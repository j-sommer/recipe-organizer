from enum import Enum
from typing import Any


class EventType(Enum):
    READ = 1
    SAVE = 2
    OPEN = 3


class Event:
    def __init__(self, event_type: EventType, payload: Any):
        self.event_type = event_type
        self.payload = payload
