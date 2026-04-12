from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running "}

@app.get("/db-check")
def db_check():
    return {"status": "DB setup ready"}