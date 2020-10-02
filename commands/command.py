from abc import abstractmethod, ABC
from enum import Enum


class CommandType(Enum):
    OPEN = 1,
    SAVE = 2


class Command(ABC):
    @property
    @abstractmethod
    def command_type(self) -> CommandType:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass
