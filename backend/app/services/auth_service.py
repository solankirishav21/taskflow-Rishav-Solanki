from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def register_user(db: Session, user_data: UserCreate):
    # check if email exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise ValueError("Email already registered")

    # create user
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user