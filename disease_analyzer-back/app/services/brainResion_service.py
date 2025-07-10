# CRUD 함수를 호출해서 실제 비즈니스 로직 처리
from crud.brainRegion_crud import get_brain_regions

def get_all_brain_regions(db):
    """
    데이터베이스에 저장된 모든 뇌 부위 정보 로드
    """
    return get_brain_regions(db)
