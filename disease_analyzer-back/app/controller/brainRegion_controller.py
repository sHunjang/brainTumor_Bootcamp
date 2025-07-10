from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.brain_region import BrainRegionSchema
from services.brainResion_service import get_all_brain_regions
from db.session import get_db

router = APIRouter()

@router.get("/brain_regions/", response_model=List[BrainRegionSchema])
def read_brain_regions(db: Session = Depends(get_db)):
    """
    DB에 저장된 모든 뇌 부위 정보를 조회
    (프론트에서 뇌 부위 설명 등에 활용)
    """
    return get_all_brain_regions(db)