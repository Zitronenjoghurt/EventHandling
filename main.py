from src.classes.spaceship import SpaceShip
from src.classes.event import Event

ss = SpaceShip()
event = Event(Event.types.DAMAGE_HULL, amount=10)
ss.publish_event(event=event)
t = 1