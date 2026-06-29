from uuid import UUID
from datetime import datetime
from typing import Optional

from .memory import (
    BaseMemory,
    MemoryType,
    Importance,
)


class BusinessIncident(BaseMemory):
    memory_type: MemoryType = MemoryType.INCIDENT

    incident_id: UUID

    title: str

    category: str

    description: str

    severity: Importance

    affected_department: Optional[str] = None

    financial_impact: Optional[float] = None

    resolution: Optional[str] = None

    incident_date: datetime