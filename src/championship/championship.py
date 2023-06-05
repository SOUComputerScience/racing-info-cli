from src.driver.driver import Driver
from src.race.race import Race
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

        self.rounds = dict() # key = race: Race, value = results: List(Driver)

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

    def getDriverStandings(self) -> List:
        '''
        get current driver standings

        returns:
        List
        '''
        sorted_standings = sorted(self.driver_standings.items(), key=lambda x:x[1])
        sorted_standings.reverse()

        printable = list()

        for i in range(len(sorted_standings)):
            printable.append(f"{i+1}: {sorted_standings[i][0].getNameFormatted()} ({sorted_standings[i][1]} points)")

        return printable

    def getTeamStandings(self) -> List:
        '''
        get current team standings

        param:
        None

        returns:
        List
        '''
        sorted_standings = sorted(self.team_standings.items(), key=lambda x:x[1])
        sorted_standings.reverse()

        printable = list()

        for i in range(len(sorted_standings)):
            printable.append(f"{i+1}: {sorted_standings[i][0].name} ({sorted_standings[i][1]} points)")

        return printable

    def holdRace(self, race: Race, results: List[Driver]):
        '''
        holds a race and updates standings given the results

        param:
        race: Race
        results: List[Driver]
        '''
        if not isinstance(race, Race):
            raise TypeError(f"{race} must be of type Race, not {type(race)}")
        
        if not self.rounds.get(race):
            self.rounds[race] = list()

            points_system = [None, 25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

            for i in range(1, 11): # only the top 10 drivers get points
                if not isinstance(results[i], Driver):
                    raise TypeError(f"{results[i]} must be of type Driver, not {type(results[i])}")
                
                # update values for driver standings and team standings

                # update driver standings

                self.driver_standings[results[i]] += points_system[i]

                if results.count(results[i]) > 1: # if this driver won fastest lap
                    self.driver_standings[results[i]] += 1

                # update team standings
                # TODO update the team standings (stretch goal???)
                
            self.rounds[race] = results