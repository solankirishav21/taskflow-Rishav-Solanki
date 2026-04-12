from pydantic import BaseModel
from uuid import UUID
from typing import Optional
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