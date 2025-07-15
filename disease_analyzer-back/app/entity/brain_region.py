from sqlalchemy import Column, Integer, String
from app.db.base import Base

class BrainRegion(Base):
    __tablename__ = 'brain_regions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    coord_x1 = Column(Integer)
    coord_y1 = Column(Integer)
    coord_x2 = Column(Integer)
    coord_y2 = Column(Integer)
    description = Column(String)
    symptom = Column(String)
