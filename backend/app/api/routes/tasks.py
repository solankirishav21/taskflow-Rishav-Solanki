from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.dependencies import get_current_user
from app.db.models.user import User
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task

router = APIRouter(tags=["Tasks"])


@router.post("/projects/{project_id}/tasks", response_model=TaskResponse)
def create_task_api(
    project_id,
    data: TaskCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return create_task(db, project_id, user, data)