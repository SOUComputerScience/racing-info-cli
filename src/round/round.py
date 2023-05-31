from src.driver.driver import Driver
from src.race.race import Race

class Round():
    def __init__(self, race: Race):
        if not isinstance(race, Race):
            raise TypeError(f"")
        
        self.race = race
        self.results = list(Driver)

    def setResults(self, results: list(Driver)):
        if not isinstance(results, list):
            raise TypeError(f"")
        
        self.results = results