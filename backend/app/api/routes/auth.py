from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import register_user
from app.schemas.user import LoginRequest, LoginResponse
from app.services.auth_service import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = register_user(db, user)
        return new_user
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "validation failed",
                "fields": {
                    "email": "already registered"
                }
            }
        )
    
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        token, user = login_user(db, data.email, data.password)

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user
        }

    except ValueError:
        raise HTTPException(
            status_code=401,
            detail={
                "error": "unauthorized",
                "fields": {
                    "credentials": "invalid email or password"
                }
            }
        )