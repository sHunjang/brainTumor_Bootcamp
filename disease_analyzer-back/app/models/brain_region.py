# 이 파일은 데이터베이스에 저장되는 '뇌 부위' 정보를 정의

from sqlalchemy import Column, Integer, String
from db.base import Base

class BrainRegion(Base):
    __tablename__ = 'brain_regions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)     # 뇌 부위명
    coord_x1 = Column(Integer)                         # 좌상단 x좌표
    coord_y1 = Column(Integer)                         # 좌상단 y좌표
    coord_x2 = Column(Integer)                         # 우하단 x좌표
    coord_y2 = Column(Integer)                         # 우하단 y좌표
    description = Column(String)                          # 주요 기능
    symptom = Column(String)                           # 종양 발생 시 증상