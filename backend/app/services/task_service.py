from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.task import Task
from app.db.models.project import Project
from app.db.models.user import User


def create_task(db: Session, project_id, user: User, data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

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

def get_tasks(db: Session, project_id, user: User, status=None, assignee=None):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    query = db.query(Task).filter(Task.project_id == project_id)

    if status:
        query = query.filter(Task.status == status)

    if assignee:
        query = query.filter(Task.assignee_id == assignee)

    return query.all()

def update_task(db: Session, task_id, user: User, data):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    project = db.query(Project).filter(Project.id == task.project_id).first()

    if project.owner_id != user.id and task.assignee_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    if data.title is not None:
        task.title = data.title

    if data.description is not None:
        task.description = data.description
    
    if data.status is not None:
        task.status = data.status

    if data.priority is not None:
        task.priority = data.priority

    if data.assignee_id is not None:
        task.assignee_id = data.assignee_id

    if data.due_date is not None:
        task.due_date = data.due_date

    db.commit()
    db.refresh(task)

    return task