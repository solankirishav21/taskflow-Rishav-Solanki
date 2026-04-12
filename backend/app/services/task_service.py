from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.task import Task
from app.db.models.project import Project
from app.db.models.user import User


def create_task(db: Session, project_id, user: User, data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    # access check (owner only for now — safe start)
    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    task = Task(
        title=data.title,
        description=data.description,
        priority=data.priority,
        assignee_id=data.assignee_id,
        due_date=data.due_date,
        project_id=project_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task