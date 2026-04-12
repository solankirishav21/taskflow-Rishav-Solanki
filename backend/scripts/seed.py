import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import uuid
from datetime import datetime, date

from app.db.session import SessionLocal
from app.db.models.user import User
from app.db.models.project import Project
from app.db.models.task import Task
from app.core.security import hash_password
from app.constants.enums import TaskStatus, TaskPriority


def run():
    db = SessionLocal()

    try:
        user = User(
            id=uuid.uuid4(),
            name="Test User",
            email="test@example.com",
            password=hash_password("password123"),
            created_at=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        project = Project(
            id=uuid.uuid4(),
            name="Sample Project",
            description="Seeded project",
            owner_id=user.id,
            created_at=datetime.utcnow()
        )
        db.add(project)
        db.commit()
        db.refresh(project)

        tasks = [
            Task(
                id=uuid.uuid4(),
                title="Task 1",
                status=TaskStatus.TODO,
                priority=TaskPriority.LOW,
                project_id=project.id,
                assignee_id=user.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            Task(
                id=uuid.uuid4(),
                title="Task 2",
                status=TaskStatus.IN_PROGRESS,
                priority=TaskPriority.MEDIUM,
                project_id=project.id,
                assignee_id=user.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
            Task(
                id=uuid.uuid4(),
                title="Task 3",
                status=TaskStatus.DONE,
                priority=TaskPriority.HIGH,
                project_id=project.id,
                assignee_id=user.id,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            ),
        ]

        db.add_all(tasks)
        db.commit()

        print("Seed data inserted successfully")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    run()