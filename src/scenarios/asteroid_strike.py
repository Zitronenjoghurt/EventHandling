from src.classes.event import Event
from src.classes.scenario import Scenario

class AsteroidStrike(Scenario):
    def execute(self) -> None:
        damage = Event(Event.TYPES.DAMAGE_HULL, amount=10)
        self.publish_event(damage)