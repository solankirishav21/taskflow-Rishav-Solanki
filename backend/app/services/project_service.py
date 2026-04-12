from sqlalchemy.orm import Session
from app.db.models.project import Project
from app.schemas.project import ProjectCreate
from app.db.models.user import User

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