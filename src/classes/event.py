from .event_types import EventTypes

class Event():
    types = EventTypes
    
    def __init__(self, type: str, **kwargs) -> None:
        self.type = type
        self.data = kwargs