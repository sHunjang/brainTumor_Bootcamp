# app/controller/imageupload_controller.py
# 사용자가 이미지를 업로드하면 AI가 종양을 탐지하고 결과 리포트를 반환 파일

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from services.ai_service import process_upload
from db.session import get_db

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    이미지 파일을 업로드하면 AI가 자동으로 종양을 탐지하고,
    위치/크기/임상 소견이 포함된 리포트를 반환

    - file: 업로드할 CT 이미지 파일
    - db: 데이터베이스 세션(자동 주입)
    """
    try:
        return await process_upload(file, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
