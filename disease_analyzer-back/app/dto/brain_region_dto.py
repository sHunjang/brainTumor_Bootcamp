from pydantic import BaseModel

class BrainRegionRequestDto(BaseModel):
    name: str
    coord_x1: int
    coord_y1: int
    coord_x2: int
    coord_y2: int
    description: str
    symptom: str

class BrainRegionResponseDto(BrainRegionRequestDto):
    id: int

    class Config:
        from_attributes = True
