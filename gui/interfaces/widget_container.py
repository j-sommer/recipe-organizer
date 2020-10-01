from abc import ABC, abstractmethod


class WidgetContainer(ABC):
    @abstractmethod
    def define_widgets(self) -> None:
        pass

    @abstractmethod
    def define_layout(self) -> None:
        pass
