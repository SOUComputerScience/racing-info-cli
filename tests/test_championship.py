from copy import deepcopy
import pytest
from src.championship.championship import Championship
from src.driver.driver import Driver
from src.race.race import Race
from src.race.raceResults import RaceResults
from src.series.series import Series
from src.team.team import Team
from tests.dummy_data import DUMMY_CHAMPIONSHIP, DUMMY_DRIVER, DUMMY_TEAM # TODO edit this later to only import used dummy vars 
from typing import Any, List

# fixtures

@pytest.fixture
def championship_fixture():
    return deepcopy(DUMMY_CHAMPIONSHIP)

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

@pytest.fixture
def team_fixture():
    return deepcopy(DUMMY_TEAM)

# test cases

def test___str__(championship_fixture: Championship):
    assert isinstance(championship_fixture, Championship)
    
    s = championship_fixture.__str__()
    
    assert isinstance(s, str)
    assert s == "Dummy Series 1011 Championship"

# addDriverToChampionship test cases

def test_addDriverToChampionship(championship_fixture: Championship, driver_fixture: Driver):
    assert isinstance(championship_fixture, Championship)
    assert isinstance(driver_fixture, Driver)

    assert isinstance(championship_fixture.driver_standings, dict)
    assert not bool(championship_fixture.driver_standings) # check if dict is empty

    championship_fixture.addDriverToChampionship(driver = driver_fixture)

    assert len(list(championship_fixture.driver_standings.keys())) == 1 # one key in dict
    assert driver_fixture in championship_fixture.driver_standings.keys() # the key is correct
    assert championship_fixture.driver_standings[driver_fixture] == 0 # the value for the key is correct

def test_addDriverToChampionship_alreadyInChampionship(championship_fixture: Championship, driver_fixture: Driver):
    assert isinstance(championship_fixture, Championship)
    assert isinstance(driver_fixture, Driver)

    assert isinstance(championship_fixture.driver_standings, dict)
    assert not bool(championship_fixture.driver_standings) # check if dict is empty

    championship_fixture.addDriverToChampionship(driver = driver_fixture)

    assert len(list(championship_fixture.driver_standings.keys())) == 1 # one key in dict
    assert driver_fixture in championship_fixture.driver_standings.keys() # the key is correct
    assert championship_fixture.driver_standings[driver_fixture] == 0 # the value for the key is correct

    # testing that there aren't now two different records for a single driver

    championship_fixture.addDriverToChampionship(driver = driver_fixture)

    assert len(list(championship_fixture.driver_standings.keys())) == 1 # one key in dict
    assert driver_fixture in championship_fixture.driver_standings.keys() # the key is correct
    assert championship_fixture.driver_standings[driver_fixture] == 0 # the value for the key is correct

# when testing behavior of an object that can hold other objects, 
# always test the behavior for when it's empty and not empty

# addTeamToChampionship test cases

def test_addTeamToChampionship_noDrivers(championship_fixture: Championship, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)
    assert isinstance(team_fixture, Team)

    assert isinstance(championship_fixture.team_standings, dict)
    assert not bool(championship_fixture.team_standings) # check if dict is empty

    championship_fixture.addTeamToChampionship(team = team_fixture)

    assert len(list(championship_fixture.team_standings.keys())) == 1 # one key in dict
    assert team_fixture in championship_fixture.team_standings.keys() # the key is correct
    assert championship_fixture.team_standings[team_fixture] == 0 # the value for the key is correct

def test_addTeamToChampionship_hasDrivers(championship_fixture: Championship, driver_fixture: Driver, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)
    assert isinstance(driver_fixture, Driver)
    assert isinstance(team_fixture, Team)

    assert isinstance(championship_fixture.driver_standings, dict)
    assert not bool(championship_fixture.driver_standings) # check if dict is empty

    assert isinstance(championship_fixture.team_standings, dict)
    assert not bool(championship_fixture.team_standings) # check if dict is empty

    team_fixture.addDriverToTeam(driver = driver_fixture)

    championship_fixture.addTeamToChampionship(team = team_fixture)

    assert len(list(championship_fixture.team_standings.keys())) == 1 # one key in dict
    assert team_fixture in championship_fixture.team_standings.keys() # the key is correct
    assert championship_fixture.team_standings[team_fixture] == 0 # the value for the key is correct

    assert len(list(championship_fixture.driver_standings.keys())) == 1 # one key in dict
    assert driver_fixture in championship_fixture.driver_standings.keys() # the key is correct
    assert championship_fixture.driver_standings[driver_fixture] == 0 # the value for the key is correct

def test_addTeamToChampionship_alreadyInChampionship(championship_fixture: Championship, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)
    assert isinstance(team_fixture, Team)

    assert isinstance(championship_fixture.team_standings, dict)

    championship_fixture.addTeamToChampionship(team = team_fixture)

    assert len(list(championship_fixture.team_standings.keys())) == 1 # one key in dict
    assert team_fixture in championship_fixture.team_standings.keys() # the key is correct
    assert championship_fixture.team_standings[team_fixture] == 0 # the value for the key is correct

    # testing that there aren't now two different records for a single team

    championship_fixture.addTeamToChampionship(team = team_fixture)

    assert len(list(championship_fixture.team_standings.keys())) == 1 # one key in dict
    assert team_fixture in championship_fixture.team_standings.keys() # the key is correct
    assert championship_fixture.team_standings[team_fixture] == 0 # the value for the key is correct

# removeDriverFromChampionship test cases

def test_removeDriverFromChampionship(championship_fixture: Championship, driver_fixture: Driver):
    assert isinstance(championship_fixture, Championship)

    pass # TODO


def test_removeDriverFromChampionship_notInChampionship(championship_fixture: Championship, driver_fixture: Driver):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

# removeTeamFromChampionship test cases

def test_removeTeamFromChampionship_noDrivers(championship_fixture: Championship, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

def test_removeTeamFromChampionship_hasDrivers(championship_fixture: Championship, driver_fixture: Driver, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

def test_removeTeamFromChampionship_notInChampionship(championship_fixture: Championship, driver_fixture: Driver, team_fixture: Team):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

# getDriverStandings test cases

def test_getDriverStandings(championship_fixture: Championship):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

# getTeamStandings test cases

def test_getTeamStandings(championship_fixture: Championship):
    assert isinstance(championship_fixture, Championship)

    pass # TODO

# holdRace test cases

def test_holdRace(championship_fixture: Championship):
    assert isinstance(championship_fixture, Championship)

    pass # TODO