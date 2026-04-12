from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.services.project_service import get_user_projects
from app.api.deps import get_db
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import create_project
from app.core.dependencies import get_current_user
from app.db.models.user import User

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("", response_model=ProjectResponse)
def create(project: ProjectCreate,
           db: Session = Depends(get_db),
           user: User = Depends(get_current_user)):
    
    return create_project(db, project, user)

@router.get("", response_model=List[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_projects(db, user)