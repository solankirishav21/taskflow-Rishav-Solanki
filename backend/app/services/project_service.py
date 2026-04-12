from sqlalchemy.orm import Session
from sqlalchemy import or_

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

def get_user_projects(db: Session, user: User):
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
        .all()
    )

    return projects