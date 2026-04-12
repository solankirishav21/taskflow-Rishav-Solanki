from fastapi import FastAPI, Depends

from app.core.dependencies import get_current_user
from app.db.models.user import User
from app.core.config import settings
from app.db.session import engine
from app.api.routes import auth

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def root():
    return {"message": f"{settings.APP_NAME} is running "}

@app.get("/db-check")
def db_check():
    return {"status": "DB setup ready"}

app.include_router(auth.router)

@app.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "id": str(user.id),
        "email": user.email,
        "name": user.name
    }