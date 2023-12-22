from typing import Callable
from .event_manager import EventManager
from .event_types import EventTypes

class EventSubscriber():
    SUBSCRIPTIONS: dict[str, Callable] = {}
    EVENT_TYPES: EventTypes

    def __init__(self) -> None:
        self.event_manager = EventManager.get_instance()
        self.init_events()

    def init_events(self):
        for event_type, listener in self.SUBSCRIPTIONS.items():
            self.event_manager.subscribe(event_type=event_type, listener=listener)

    def publish_event(self, event):
        self.event_manager.publish(event=event)