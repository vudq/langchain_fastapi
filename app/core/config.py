from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "HR Agents API"
    APP_VERSION: str = "1.0.0"
    
    # Project Settings
    PROJECT_NAME: str = "HR Agents"
    DESCRIPTION: str = "Unified API for HR-related services"
    VERSION: str = "1.0.0"
    
    # Model settings
    MODEL_NAME: str = "gemini-2.0-flash"
    MODEL_TEMPERATURE: float = 0.7
    GOOGLE_API_KEY: Optional[str] =  "" #os.getenv("GOOGLE_API_KEY")

    # Template settings
    TEMPLATES_DIR: str = "app/templates"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 
