from enum import Enum
from typing import Any


class EventType(Enum):
    FILE_READ = 1
    SAVED = 2
    SOURCE_SET = 3


class Event:
    def __init__(self, event_type: EventType, payload: Any):
        self.event_type = event_type
        self.payload = payload
