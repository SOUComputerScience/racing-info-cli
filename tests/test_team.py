from copy import deepcopy
import pytest
from src.driver.driver import Driver
from src.team.team import Team
from tests.dummy_data import DUMMY_DRIVER, DUMMY_DRIVER_TWO, DUMMY_TEAM

# Fixtures

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

@pytest.fixture
def driver_fixture_two():
    return deepcopy(DUMMY_DRIVER_TWO)

@pytest.fixture
def team_fixture():
    return deepcopy(DUMMY_TEAM)

# Test Cases

def test_addDriverToTeam(team_fixture: Team, driver_fixture: Driver):
    assert isinstance(team_fixture, Team)
    assert isinstance(driver_fixture, Driver)

    assert len(team_fixture.drivers) == 0
    team_fixture.addDriverToTeam(driver_fixture)

    assert len(team_fixture.drivers) == 1
    assert team_fixture.drivers[0] == driver_fixture

    team_fixture.addDriverToTeam(driver_fixture)
    assert len(team_fixture.drivers) == 1

def test_removeDriverFromTeam(team_fixture: Team, driver_fixture: Driver, driver_fixture_two: Driver):
    team_fixture = team_fixture

    assert isinstance(driver_fixture, Driver)
    assert isinstance(driver_fixture_two, Driver)
    assert isinstance(team_fixture, Team)

    assert len(team_fixture.drivers) == 0
    team_fixture.addDriverToTeam(driver_fixture)

    assert len(team_fixture.drivers) == 1
    assert team_fixture.drivers[0] == driver_fixture

    team_fixture.removeDriverFromTeam(driver_fixture_two)
    assert len(team_fixture.drivers) == 1

    team_fixture.removeDriverFromTeam(driver_fixture)
    assert len(team_fixture.drivers) == 0

def test_getDrivers(team_fixture: Team, driver_fixture: Driver):
    assert isinstance(team_fixture, Team)

    assert len(team_fixture.getDrivers()) == 0

    team_fixture.addDriverToTeam(driver = driver_fixture)

    drivers = team_fixture.getDrivers()

    assert isinstance(drivers, list)
    assert len(drivers) == 1
    
    assert isinstance(drivers[0], Driver)
    assert drivers[0] == driver_fixture