from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

from app.schemas.task import TaskResponse
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    owner_id: UUID
    class Config:
        from_attributes = True

class ProjectDetailResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    owner_id: UUID
    tasks: List[TaskResponse]

    class Config:
        from_attributes = True