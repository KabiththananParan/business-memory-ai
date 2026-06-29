from enum import Enum
from uuid import UUID
from datetime import datetime
from typing import List

from .memory import (
    BaseMemory,
    MemoryType,
)


class MeetingType(str, Enum):
    BOARD = "board"
    MANAGEMENT = "management"
    SUPPLIER = "supplier"
    CUSTOMER = "customer"


class MeetingMemory(BaseMemory):
    memory_type: MemoryType = MemoryType.MEETING

    meeting_id: UUID

    meeting_type: MeetingType

    title: str

    participants: List[str]

    summary: str

    decisions: List[str]

    action_items: List[str]

    meeting_date: datetime