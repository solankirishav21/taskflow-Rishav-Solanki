from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):

    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int

    class Config:
        env_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            ".env"
        )
        extra = "allow"

settings = Settings()