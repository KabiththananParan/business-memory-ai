from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class MemoryType(str, Enum):
    SUPPLIER = "supplier"
    CUSTOMER = "customer"
    MEETING = "meeting"
    INCIDENT = "incident"
    
class Importance(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    
class Status(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class SourceType(str, Enum):
    MANUAL = "manual"
    EMAIL = "email"
    MEETING = "meeting"
    API = "api"
    SYSTEM = "system"
    
class BaseMemory(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    memory_type: MemoryType
    importance: Importance = Importance.MEDIUM
    status: Status = Status.OPEN
    source: SourceType = SourceType.MANUAL
    tags: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None



