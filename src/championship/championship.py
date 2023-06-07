from src.driver.driver import Driver
from src.race.race import Race
from src.race.raceResults import RaceResults
from src.series.series import Series
from src.team.team import Team
from typing import List

class Championship():
    """
    a class to represent a series championship.
    associated with a series (e.g. Formula One, IndyCar, Nascar) and a year (e.g. 2022, 2023)
    """
    def __init__(self, series: Series, year: int):
        if not isinstance(series, Series):
            raise TypeError(f"{series} must be of type Series, not {type(series)}")
        if not isinstance(year, int):
            raise TypeError(f"{year} must be of type int, not {type(year)}")
        
        self.series = series
        self.year = year

        self.race_results = list() # list of RaceResults objects

        self.driver_standings = dict()
        self.team_standings = dict()

    def addDriverToChampionship(self, driver: Driver):
        """
        adds a driver or a list of drivers to the championship

        params:
        driver: Driver
        """
        if not isinstance(driver, Driver):
            raise TypeError(f"{driver} must be of type Driver, not {type(driver)}")
        
        if not self.driver_standings.get(driver):
            self.driver_standings[driver] = 0

    def addTeamToChampionship(self, team: Team):
        """
        adds a team to the championship

        params:
        team: Team
        """
        if not isinstance(team, Team):
            raise TypeError(f"{team} must be of type Team, not {type(team)}")

        self.team_standings[team] = 0 # add team to team standings, set points to 0

        for d in team.drivers: # for each of the team's drivers
            if not isinstance(d, Driver):
                raise TypeError(f"{d} must be of type Driver, not {type(d)}")

            if not self.driver_standings.get(d): # if driver is not already in driver's championship
                self.addDriverToChampionship(d) # add to driver's championship

    def removeTeamFromChampionship(self, team: Team):
        """
        adds a team or a list of teams to the championship

        params:
        team: Team
        """
        if not isinstance(team, Team):
            raise TypeError(f"{team} must be of type Team, not {type(team)}")
        
        if self.team_standings.get(team):
            self.team_standings.pop(team)

    def getDriverStandings(self) -> List[str]:
        '''
        get current driver standings

        returns:
        List[str]
        '''
        sorted_standings = sorted(self.driver_standings.items(), key=lambda x:x[1])
        sorted_standings.reverse()

        printable = list()

        for i in range(len(sorted_standings)):
            printable.append(f"{i+1}: {sorted_standings[i][0].__str__()} ({sorted_standings[i][1]} points)")

        return printable

    def getTeamStandings(self) -> List[str]:
        '''
        get current team standings

        returns:
        List[str]
        '''
        sorted_standings = sorted(self.team_standings.items(), key=lambda x:x[1])
        sorted_standings.reverse()

        printable = list()

        for i in range(len(sorted_standings)):
            printable.append(f"{i+1}: {sorted_standings[i][0].name} ({sorted_standings[i][1]} points)")

        return printable

    def holdRace(self, race_results: RaceResults):
        '''
        holds a race and updates standings given the results

        params:
        race_results: RaceResults
        '''

        # type checking

        if not isinstance(race_results, RaceResults):
            raise TypeError(f"{race_results} must be of type RaceResults, not {type(race_results)}")
        
        if not isinstance(race_results.race, Race):
            raise TypeError(f"{race_results.race} must be of type Race, not {type(race_results.race)}")
        
        if not isinstance(race_results.results, dict):
            raise TypeError(f"{race_results.results} must be of type dict, not {type(race_results.results)}")

        # TODO update standings based on the results