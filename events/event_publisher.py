from typing import List

from events.event_observer import EventObserver

_observers: List[EventObserver] = []


class EventPublisher:

    @staticmethod
    def add(observer):
        _observers.append(observer)

    @staticmethod
    def remove(observer):
        _observers.remove(observer)

    @staticmethod
    def broadcast(event):
        for observer in _observers:
            observer.notify(event)
