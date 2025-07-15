import shutil
import os
import uuid
from .yolo_service import predict_and_generate_report
from app.config.settings import settings

UPLOAD_DIR = settings.UPLOAD_DIR
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def process_upload(file, db):
    task_id = str(uuid.uuid4())
    temp_file_path = os.path.join(UPLOAD_DIR, f"{task_id}_{file.filename}")
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        result = predict_and_generate_report(temp_file_path, db, save_image=True)
        return result
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
