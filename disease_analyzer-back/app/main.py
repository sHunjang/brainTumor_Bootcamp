from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from controller import imgUpload_controller, brainRegion_controller

# FastAPI 서버 생성
app = FastAPI()


# 프론트(React) 연결을 위함
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # '*' 사용시 전체 허용, 배포시 도메인 지정 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 업로드/결과 이미지 정적 파일 서빌
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# 각 기능별 라우터를 등록
# 이미지 업로드 페이지 라우터
app.include_router(imgUpload_controller.router, prefix="/api")
# 종양 CT 결과 출력 페이지 라우터
app.include_router(brainRegion_controller.router, prefix="/api")



@app.get("/")
def root():
    return {"message": "뇌종양 자동 진단 AI API"}
