from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional, List

from app.schemas.task import TaskResponse
class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    description: Optional[str]
    owner_id: UUID

class ProjectDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    description: Optional[str]
    owner_id: UUID
    tasks: List[TaskResponse]

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None