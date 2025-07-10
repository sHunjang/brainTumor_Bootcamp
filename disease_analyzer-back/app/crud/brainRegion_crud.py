# 데이터베이스에서 뇌 부위 정보 로드

from sqlalchemy.orm import Session
from models.brain_region import BrainRegion

def get_brain_regions(db: Session):
    """
    모든 뇌 부위 정보를 리스트로 반환합니다.
    """
    return db.query(BrainRegion).all()
