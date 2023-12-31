from .event import Event
from .event_subscriber import EventSubscriber

class SpaceShip(EventSubscriber):
    def __init__(self) -> None:
        self.SUBSCRIPTIONS = {
            Event.TYPES.DAMAGE_HULL: self.damage_hull
        }
        super().__init__()
        self.hull = 100

    def damage_hull(self, amount: int) -> None:
        self.hull -= amount