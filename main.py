from src.classes.scenario import Scenario, ScenarioFactory
from src.classes.spaceship import SpaceShip
from src.classes.event import Event

ss = SpaceShip()

# takes 10 hull damage through direct event
event = Event(Event.TYPES.DAMAGE_HULL, amount=10)
ss.publish_event(event=event)

# takes 10 hull damage through scenario
scenario_library = ScenarioFactory.get_instance()
asteroid_strike = scenario_library.get_scenario(Scenario.TYPES.ASTEROID_STRIKE)
asteroid_strike.execute()