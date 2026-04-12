from fastapi import APIRouter, Depends, Response, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectDetailResponse, ProjectUpdate
from app.services.project_service import create_project, get_project_by_id, get_user_projects, update_project, delete_project, get_project_stats
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
    page: int = Query(1, ge = 1),
    limit: int = Query(10, le = 100),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_user_projects(db, user, page, limit)

@router.get("/{project_id}", response_model=ProjectDetailResponse)
def get_project(
    project_id,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_project_by_id(db, project_id, user)


@router.patch("/{project_id}", response_model=ProjectResponse)
def update(
    project_id,
    data: ProjectUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return update_project(db, project_id, user, data)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    project_id,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    delete_project(db, project_id, user)
    return Response(status_code=204)

from app.services.project_service import get_project_stats


@router.get("/{project_id}/stats")
def project_stats(
    project_id,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_project_stats(db, project_id, user)