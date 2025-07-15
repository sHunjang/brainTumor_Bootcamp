from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.ai_service import process_upload
from app.db.connection import get_db

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        return await process_upload(file, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
