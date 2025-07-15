from ultralytics import YOLO
from app.repository.brain_region_repository import get_all_brain_regions
import cv2
import os
from app.config.settings import settings
import shutil

model = YOLO(settings.MODEL_PATH)
RESULT_DIR = settings.UPLOAD_DIR

def map_to_brain_region(box_xyxy, brain_regions):
    x1, y1, x2, y2 = box_xyxy
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    for region in brain_regions:
        if region.coord_x1 <= cx <= region.coord_x2 and region.coord_y1 <= cy <= region.coord_y2:
            return region
    return None

def generate_clinical_note(region):
    if region:
        return (
            f"{region.name}은(는) {region.description}을(를) 담당합니다. "
            f"해당 부위에 종양이 발생하면 {region.symptom} 등이 나타날 수 있습니다."
        )
    else:
        return "탐지된 위치의 임상적 기능 정보가 부족합니다."

def predict_and_generate_report(image_path, db_session, save_image=False):
    results = model.predict(image_path)
    result = results[0]
    brain_regions = get_all_brain_regions(db_session)
    report_data = None
    img = cv2.imread(image_path)

    for box in result.boxes:
        xyxy = box.xyxy.tolist()
        if isinstance(xyxy[0], list):
            x1, y1, x2, y2 = map(int, xyxy[0])
        else:
            x1, y1, x2, y2 = map(int, xyxy)
        confs = box.conf.tolist()
        conf = float(confs[0]) if isinstance(confs, list) else float(confs)
        region = map_to_brain_region((x1, y1, x2, y2), brain_regions)
        clinical_note = generate_clinical_note(region)
        region_name = region.name if region else "알 수 없음"
        description = region.description if region else ""
        symptom = region.symptom if region else ""
        size = f"{abs(x2-x1)}px x {abs(y2-y1)}px"
        coords = f"{x1}, {y1}, {x2}, {y2}"

        if img is None:
            raise ValueError("이미지 파일을 읽을 수 없습니다.")
        
        if save_image and img is not None:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            result_img_name = f"result_{os.path.basename(image_path)}"
            result_img_path = os.path.join(RESULT_DIR, result_img_name)
            cv2.imwrite(result_img_path, img)
            image_url = f"/uploads/{result_img_name}"
        else:
            image_url = f"/uploads/{os.path.basename(image_path)}"

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
            "coord_x1": region.coord_x1 if region else "",
            "coord_y1": region.coord_y1 if region else "",
            "coord_x2": region.coord_x2 if region else "",
            "coord_y2": region.coord_y2 if region else "",
            "description": region.description if region else "",
            "symptom": region.symptom if region else "",
        }
        break

    if not report_data:
        # 종양이 없는 경우에도 원본 이미지 복사
        result_img_name = f"result_{os.path.basename(image_path)}"
        result_img_path = os.path.join(RESULT_DIR, result_img_name)
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
