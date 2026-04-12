from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, func

from app.db.models.project import Project
from app.schemas.project import ProjectCreate
from app.db.models.user import User
from app.db.models.task import Task

def create_project(db: Session, project_data: ProjectCreate, user: User):
    project = Project(
        name=project_data.name,
        description=project_data.description,
        owner_id=user.id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project

def get_user_projects(db: Session, user: User, page:1, limit=10):
    offset = (page - 1) * limit
    projects = (
        db.query(Project)
        .outerjoin(Task, Task.project_id == Project.id)
        .filter(
            or_(
                Project.owner_id == user.id,
                Task.assignee_id == user.id
            )
        )
        .distinct()
        .offset(offset)
        .limit(limit)
        .all()
    )

    return projects

def get_project_by_id(db: Session, project_id, user: User):
    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    has_access = (
        project.owner_id == user.id or
        db.query(Task)
        .filter(Task.project_id == project_id, Task.assignee_id == user.id)
        .first()
    )

    if not has_access:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    return project

def update_project(db: Session, project_id, user: User, data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    if data.name is not None:
        project.name = data.name

    if data.description is not None:
        project.description = data.description

    db.commit()
    db.refresh(project)

    return project

def delete_project(db: Session, project_id, user: User):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    db.delete(project)
    db.commit()

def get_project_stats(db: Session, project_id, user: User):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail={"error": "not found"})

    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail={"error": "forbidden"})

    status_counts = (
        db.query(Task.status, func.count(Task.id))
        .filter(Task.project_id == project_id)
        .group_by(Task.status)
        .all()
    )

    assignee_counts = (
        db.query(Task.assignee_id, func.count(Task.id))
        .filter(Task.project_id == project_id)
        .group_by(Task.assignee_id)
        .all()
    )

    return {
        "by_status": {status: count for status, count in status_counts},
        "by_assignee": {
            str(assignee): count for assignee, count in assignee_counts if assignee
        }
    }