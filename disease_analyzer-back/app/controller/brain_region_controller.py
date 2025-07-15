from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.services.brain_region_service import BrainRegionService
from app.dto.brain_region_dto import BrainRegionRequestDto, BrainRegionResponseDto
from app.db.connection import get_db

router = APIRouter(
    prefix="/api/brain-regions",
    tags=["brain-regions"]
)

def get_brain_region_service(db: Session = Depends(get_db)) -> BrainRegionService:
    return BrainRegionService(db)

@router.post("/", response_model=BrainRegionResponseDto, status_code=status.HTTP_201_CREATED)
def create_brain_region(
    brain_region_dto: BrainRegionRequestDto,
    service: BrainRegionService = Depends(get_brain_region_service)
) -> BrainRegionResponseDto:
    return service.create_brain_region(brain_region_dto)

@router.get("/{brain_region_id}", response_model=BrainRegionResponseDto)
def get_brain_region(
    brain_region_id: int,
    service: BrainRegionService = Depends(get_brain_region_service)
) -> BrainRegionResponseDto:
    brain_region = service.get_brain_region_by_id(brain_region_id)
    if not brain_region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brain region not found")
    return brain_region

@router.get("/", response_model=List[BrainRegionResponseDto])
def get_all_brain_regions(
    service: BrainRegionService = Depends(get_brain_region_service)
) -> List[BrainRegionResponseDto]:
    return service.get_all_brain_regions()

@router.delete("/{brain_region_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brain_region(
    brain_region_id: int,
    service: BrainRegionService = Depends(get_brain_region_service)
):
    if not service.delete_brain_region(brain_region_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brain region not found")
