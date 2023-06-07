from copy import deepcopy
import pytest
from src.driver.driver import Driver
from src.engine.engine import *
from src.team.team import Team
from tests.dummy_data import DUMMY_DRIVER, DUMMY_DRIVER_TWO, DUMMY_TEAM

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

@pytest.fixture
def team_fixture():
    return deepcopy(DUMMY_TEAM)

def test_addDriverToTeam(team_fixture: Team, driver_fixture: Driver):
    assert isinstance(team_fixture, Team)
    assert isinstance(driver_fixture, Driver)

    assert len(team_fixture.drivers) == 0
    team_fixture.addDriverToTeam(driver_fixture)

    assert len(team_fixture.drivers) == 1
    assert team_fixture.drivers[0] == driver_fixture

    team_fixture.addDriverToTeam(driver_fixture)
    assert len(team_fixture.drivers) == 1

def test_removeDriverFromTeam(team_fixture: Team, driver_fixture: Driver):
    team_fixture = team_fixture

    assert isinstance(team_fixture, Team)
    assert isinstance(driver_fixture, Driver)

    assert len(team_fixture.drivers) == 0
    team_fixture.addDriverToTeam(driver_fixture)

    assert len(team_fixture.drivers) == 1
    assert team_fixture.drivers[0] == driver_fixture

    team_fixture.removeDriverFromTeam(DUMMY_DRIVER_TWO)
    assert len(team_fixture.drivers) == 1

    team_fixture.removeDriverFromTeam(driver_fixture)
    assert len(team_fixture.drivers) == 0