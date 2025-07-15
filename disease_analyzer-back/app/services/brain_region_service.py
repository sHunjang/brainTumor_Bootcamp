from app.repository.brain_region_repository import (
    get_all_brain_regions,
    get_brain_region_by_id,
    create_brain_region,
    delete_brain_region
)
from app.dto.brain_region_dto import BrainRegionRequestDto, BrainRegionResponseDto

class BrainRegionService:
    def __init__(self, db):
        self.db = db

    def create_brain_region(self, brain_region_dto: BrainRegionRequestDto) -> BrainRegionResponseDto:
        region = create_brain_region(self.db, brain_region_dto)
        return BrainRegionResponseDto.from_orm(region)

    def get_brain_region_by_id(self, brain_region_id: int) -> BrainRegionResponseDto:
        region = get_brain_region_by_id(self.db, brain_region_id)
        if region:
            return BrainRegionResponseDto.from_orm(region)
        return None

    def get_all_brain_regions(self) -> list[BrainRegionResponseDto]:
        regions = get_all_brain_regions(self.db)
        return [BrainRegionResponseDto.from_orm(r) for r in regions]

    def delete_brain_region(self, brain_region_id: int) -> bool:
        return delete_brain_region(self.db, brain_region_id)
