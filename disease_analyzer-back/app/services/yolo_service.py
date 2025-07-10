from ultralytics import YOLO
import cv2
import os
import shutil

from crud.brainRegion_crud import get_brain_regions

MODEL_PATH = 'model/best.pt'
RESULT_DIR = "uploads"

# 학습한 YOLO 모델 로드
model = YOLO(MODEL_PATH)


def map_to_brain_region(box_xyxy, brain_regions):
    '''
    AI가 찾은 종양의 위치(박스 중심 좌표)가 어느 뇌 부위에 해당하는지 DB 정보와 비교
    - box_xyxy: [x1, y1, x2, y2] (종양 영역의 좌상단/우하단 좌표)
    - brain_regions: DB에서 불러온 뇌 부위 정보 리스트
    '''
    x1, y1, x2, y2 = box_xyxy
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # 박스 중심 좌표 계산

    for region in brain_regions:
        # 중심 좌표가 해당 뇌 부위의 범위 내에 있으면 해당 부위로 매핑
        if region.coord_x1 <= cx <= region.coord_x2 and region.coord_y1 <= cy <= region.coord_y2:
            return region
    
    return None   # 해당 없음

def generate_clinical_note(region):
    '''
    뇌 부위에 따라 자동으로 임상 소견(예상 증상 등)을 생성
    '''
    if region:
        return (
            f"{region.name}은(는) {region.description}을(를) 담당함))"
            f"해당 부위에 종양이 발생하면 {region.symptom} 등이 나타날 수 있음"
        )
    else:
        return "탐지된 위치의 임상적 기능 정보가 부족"
    

def predict_and_generate_report(image_path, db_session, save_image=False):
    """
    1. 이미지를 AI 모델에 입력해 종양을 탐지
    2. 각 종양의 위치를 DB의 뇌 부위 정보와 매핑
    3. 부위별 임상 소견을 포함한 리포트 생성
    """
    results = model.predict(image_path)
    result = results[0]  # 단일 이미지
    brain_regions = get_brain_regions(db_session)
    report_data = None
    img = cv2.imread(image_path)

    for box in result.boxes:
        # 좌표 추출
        xyxy = box.xyxy.tolist()
        if isinstance(xyxy[0], list):
            x1, y1, x2, y2 = map(int, xyxy[0])
        else:
            x1, y1, x2, y2 = map(int, xyxy)

        # 신뢰도 추출
        confs = box.conf.tolist()
        conf = float(confs[0]) if isinstance(confs, list) else float(confs)

        region = map_to_brain_region((x1, y1, x2, y2), brain_regions)
        clinical_note = generate_clinical_note(region)
        region_name = region.name if region else "알 수 없음"
        size = f"{abs(x2-x1)}px x {abs(y2-y1)}px"
        coords = f"{x1}, {y1}, {x2}, {y2}"

        if save_image and img is not None:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            result_img_name = f"result_{os.path.basename(image_path)}"
            result_img_path = os.path.join(RESULT_DIR, result_img_name)
            cv2.imwrite(result_img_path, img)
            image_url = f"/uploads/{result_img_name}"
        else:
            image_url = ""

        report_data = {
            "image_url": image_url,
            "diagnosis": "뇌종양" if region else "정상",
            "location": region_name,
            "coords": coords,
            "size": size,
            "confidence": f"{conf*100:.1f}%",
            "comment": clinical_note,
            "bbox_top": y1,
            "bbox_left": x1,
            "bbox_width": x2 - x1,
            "bbox_height": y2 - y1,
            # 아래 4개: DB의 원본 좌표 정보
            "coord_x1": region.coord_x1 if region else "",
            "coord_y1": region.coord_y1 if region else "",
            "coord_x2": region.coord_x2 if region else "",
            "coord_y2": region.coord_y2 if region else "",
            # 주요 기능(설명)
            "description": region.description if region else "",
            # 예상 증상
            "symptom": region.symptom if region else "",
        }
        break

    if not report_data:
        # 종양이 없는 경우에도 이미지 파일을 uploads 폴더에 저장
        result_img_name = f"result_{os.path.basename(image_path)}"
        result_img_path = os.path.join(RESULT_DIR, result_img_name)
        # 이미지가 이미 uploads에 있지 않다면 복사
        if not os.path.exists(result_img_path):
            shutil.copy(image_path, result_img_path)
        image_url = f"/uploads/{result_img_name}"
        report_data = {
            "image_url": image_url,
            "diagnosis": "정상",
            "location": "없음",
            "coords": "",
            "size": "",
            "confidence": "",
            "comment": "종양이 탐지되지 않았습니다.",
            "bbox_top": 0,
            "bbox_left": 0,
            "bbox_width": 0,
            "bbox_height": 0,
            "coord_x1": "",
            "coord_y1": "",
            "coord_x2": "",
            "coord_y2": "",
            "description": "",
            "symptom": "",
        }
    return report_data