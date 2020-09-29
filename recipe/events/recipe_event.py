from enum import Enum
from typing import Any


class RecipeEventType(Enum):
    READ = 1
    SAVE = 2


class RecipeEvent:
    def __init__(self, event_type: RecipeEventType, payload: Any):
        self.event_type = event_type
        self.payload = payload
