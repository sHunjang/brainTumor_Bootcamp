# 이 파일은 API 요청/응답 데이터의 구조 정의

from pydantic import BaseModel

class BrainRegionSchema(BaseModel):
    id: int
    name: str
    coord_x1: int
    coord_y1: int
    coord_x2: int
    coord_y2: int
    description: str
    symptom: str

    class Config:
        orm_mode = True  # SQLAlchemy 모델과 연동을 쉽게 해줍니다.
