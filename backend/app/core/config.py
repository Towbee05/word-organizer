from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    
    STORAGE_BACKEND: str = "local"
    STORAGE_UPLOAD_DIR: Path = BASE_DIR / "storage" / "uploads"

    ALLOWED_CONTENT_TYPES: set[str] = {
        "application/msword", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/pdf"
    }

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )



settings = Settings()