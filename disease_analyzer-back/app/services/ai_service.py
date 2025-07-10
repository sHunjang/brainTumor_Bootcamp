import shutil
import os
import uuid
from services.yolo_service import predict_and_generate_report

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # 업로드 폴더가 없으면 자동 생성

async def process_upload(file, db):
    '''
    1. 업로드된 이미지를 임시 폴더에 저장
    2. AI 모델로 예측 및 리포트 생성
    3. 임시 파일 삭제 후 결과 반화
    '''
    tast_id = str(uuid.uuid4())   # 각 요청마다 고유한 ID 생성
    temp_file_path = os.path.join(UPLOAD_DIR, f"{tast_id}_{file.filename}")
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)   # 파일 저장
    
    try:
        result = predict_and_generate_report(temp_file_path, db, save_image=True)   # AI 예측 및 리포트 생성
        # result에 image_url 등 프론트랑 통신하려면 필드 포함되어야 함
        return result
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
