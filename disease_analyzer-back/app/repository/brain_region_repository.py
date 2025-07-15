from sqlalchemy.orm import Session
from app.entity.brain_region import BrainRegion

def get_all_brain_regions(db: Session):
    return db.query(BrainRegion).all()

def get_brain_region_by_id(db: Session, brain_region_id: int):
    return db.query(BrainRegion).filter(BrainRegion.id == brain_region_id).first()

def create_brain_region(db: Session, dto):
    region = BrainRegion(**dto.dict())
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

def delete_brain_region(db: Session, brain_region_id: int):
    region = get_brain_region_by_id(db, brain_region_id)
    if region:
        db.delete(region)
        db.commit()
        return True
    return False
