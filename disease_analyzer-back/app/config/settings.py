# app/config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "mysql+pymysql://root:1234@localhost/disease_analyzer"
    UPLOAD_DIR: str = "uploads"
    MODEL_PATH: str = "app/ai/best.pt"

settings = Settings()
