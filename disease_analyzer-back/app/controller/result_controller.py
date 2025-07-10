from fastapi import APIRouter, HTTPException

router = APIRouter()

# 예시: 메모리/DB에 결과 저장 시 사용
RESULTS = {}

@router.get("/result/{task_id}")
def get_result(task_id: str):
    """
    task_id로 AI 예측 결과(리포트)를 조회 API
    """
    if task_id not in RESULTS:
        raise HTTPException(status_code=404, detail="결과를 찾을 수 없습니다.")
    return {"report": RESULTS[task_id]}
