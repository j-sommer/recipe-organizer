from abc import abstractmethod, ABC
from enum import Enum


class CommandType(Enum):
    NEW = 1,
    OPEN = 2,
    SAVE = 3


class Command(ABC):
    @property
    @abstractmethod
    def command_type(self) -> CommandType:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass
