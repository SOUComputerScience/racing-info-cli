from src.driver.driver import Driver
from src.race.race import Race
from src.team.team import Team
from typing import List

class RaceResults():
    def __init__(self, race: Race, rankings: List[Driver], fastestLap: Driver):
        if not isinstance(race, Race):
            raise TypeError(f"{race} must be of type Race, not {type(race)}")
        if not isinstance(rankings, List):
            raise TypeError(f"{rankings} must be of type List, not {type(rankings)}")
        if not isinstance(fastestLap, Driver):
            raise TypeError(f"{fastestLap} must be of type Driver, not {type(fastestLap)}")
        
        self.race = race
        self.results = dict() # key = driver: Driver, value = points: int
        
        # calculate points

        points_system = [None, 25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(1,21):
            if not isinstance(rankings[i], Driver):
                raise TypeError(f"{rankings[i]} must be of type Driver, not {type(rankings[i])}")
            
            self.results[rankings[i]] = points_system[i]

        if self.results[fastestLap] > 0: # if the driver who got the fastest lap finished in the points
            self.results[fastestLap] += 1 # give them an extra point for fastest lap


    def getPointsForDriver(self, driver: Driver) -> int:
        if not isinstance(driver, Driver):
            raise TypeError(f"{driver} must be of type Driver, not {type(driver)}")
        
        return self.results[driver]
    
    def getPointsForTeam(self, team: Team) -> int:
        if not isinstance(team, Team):
            raise TypeError(f"{team} must be of type Team, not {type(team)}")
        
        points = 0
        for driver in team.drivers:
            points += self.getPointsForDriver(driver)
        
        return points