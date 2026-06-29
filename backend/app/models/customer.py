from uuid import UUID
from datetime import datetime
from typing import Optional

from .memory import (
    BaseMemory,
    MemoryType,
    Importance,
)


class CustomerMemory(BaseMemory):
    memory_type: MemoryType = MemoryType.CUSTOMER

    customer_id: UUID

    customer_name: str

    customer_segment: str

    issue_type: str

    description: str

    revenue_impact: Optional[float] = None

    importance: Importance

    created_date: datetime