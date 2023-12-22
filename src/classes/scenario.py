import importlib
import inspect
import os
import sys

from .event_subscriber import EventSubscriber
from ..constants.scenario_types import ScenarioTypes

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SCENARIO_DIR = os.path.join(CURRENT_DIR, '..', 'scenarios')

class Scenario(EventSubscriber):
    TYPES = ScenarioTypes

    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> None:
        return
    
class ScenarioFactory():
    _instance = None

    def __init__(self) -> None:
        self.scenarios: dict[str, Scenario] = {}
        self.load_scenarios()
    
    @staticmethod
    def get_instance() -> 'ScenarioFactory':
        if ScenarioFactory._instance is None:
            ScenarioFactory._instance = ScenarioFactory()
        return ScenarioFactory._instance
    
    def load_scenarios(self) -> None:
        scenarios = {}
        sys.path.insert(0, SCENARIO_DIR)

        for file in os.listdir(SCENARIO_DIR):
            if file.endswith('.py') and file != '__init__.py':
                module_name = file[:-3]
                module = importlib.import_module(module_name)

                for name, cls in inspect.getmembers(module):
                    if inspect.isclass(cls) and cls.__module__ == module.__name__:
                        scenarios[name] = cls()

        sys.path.pop(0)
        self.scenarios = scenarios

    def get_scenario(self, scenario_type: str) -> Scenario:
        scenario = self.scenarios.get(scenario_type, None)

        if not scenario:
            raise ValueError(f"Scenario {scenario} does not exist.")
        
        return scenario