from uuid import UUID
from datetime import datetime
from typing import Optional

from .memory import (
    BaseMemory,
    MemoryType,
    Importance,
)


class SupplierMemory(BaseMemory):
    memory_type: MemoryType = MemoryType.SUPPLIER

    supplier_id: UUID

    supplier_name: str

    incident_type: str

    description: str

    severity: Importance

    financial_impact: Optional[float] = None

    incident_date: datetime