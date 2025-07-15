from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.controller import imgUpload_controller, brain_region_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 시에는 도메인 지정 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(imgUpload_controller.router, prefix="/api")
app.include_router(brain_region_controller.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "뇌종양 자동 진단 AI API"}
