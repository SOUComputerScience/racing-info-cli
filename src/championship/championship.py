from src.driver.driver import Driver
from src.race.race import Race
from src.round.round import Round
from src.series.series import Series
from src.team.team import Team
from typing import List

class Championship():
    def __init__(self, series: Series, year: int):
        if not isinstance(series, Series):
            raise TypeError(f"")
        if not isinstance(year, int):
            raise TypeError(f"")
        
        self.series = series
        self.year = year

        self.rounds = dict() # the key = race: Race, value = results: List(Driver)

        self.driver_standings = dict()
        self.team_standings = dict()

    def addDriverToChampionship(self, driver: Driver):
        """
        """
        if not isinstance(driver, Driver):
            raise TypeError(f"")
        
        if not self.driver_standings.get(driver):
            self.driver_standings[driver] = 0

    def addTeamToChampionship(self, team: Team):
        """
        """
        if not isinstance(team, Team):
            raise TypeError(f"")

        self.team_standings[team] = 0 # add team to team standings, set points to 0

        for d in team.drivers: # for each of the team's drivers
            if not isinstance(d, Driver):
                raise TypeError(f"")

            if not self.driver_standings.get(d): # if driver is not already in driver's championship
                self.addDriverToChampionship(d) # add to driver's championship

    def getDriverStandings(self) -> List:
        '''
        get current driver standings
        '''
        # TODO
        pass

    def getTeamStandings(self) -> List:
        '''
        get current team standings
        '''
        # TODO
        pass

    def holdRace(self, race: Race, results: List[Driver]):
        if not isinstance(race, Race):
            raise TypeError(f"")
        
        if not self.rounds.get(race):
            self.rounds[race] = list()

            points_system = [None, 25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

            for i in range(1, 11): # only the top 10 drivers get points
                if not isinstance(results[i], Driver):
                    raise TypeError(f"")
                
                # update values for driver standings and team standings

                # update driver standings

                self.driver_standings[results[i]] += points_system[i]

                if results.count(results[i]) > 1: # if this driver won fastest lap
                    self.driver_standings[results[i]] += 1

                # update team standings
                # TODO
                
            self.rounds[race] = results