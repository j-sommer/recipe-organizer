from tkinter import Frame, Label

from events.event import EventType, Event
from events.event_observer import EventObserver
from events.event_publisher import EventPublisher


class EventDisplay(Frame, EventObserver):
    _label_event_message: Label = None

    _event_message = {
        EventType.FILE_READ: "Rezept geöffnet",
        EventType.SAVED: "Rezept gespeichert"
    }

    def __init__(self):
        super().__init__()

        EventPublisher.add(self)

    def notify(self, event: Event) -> None:
        if event.event_type in self._event_message:
            if self._label_event_message is not None:
                self._label_event_message.destroy()

            self.create_short_lived_label_with_message(self._event_message.get(event.event_type))

    def create_short_lived_label_with_message(self, text: str):
        self._label_event_message = Label(self, text=f"- {text} -")
        self._label_event_message.grid(row=0)
        self.after(3000, self._label_event_message.destroy)
