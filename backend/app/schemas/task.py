from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import date

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    status: str
    priority: str
    assignee_id: Optional[UUID]
    due_date: Optional[date]

    class Config:
        from_attributes = True