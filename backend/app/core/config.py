from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()