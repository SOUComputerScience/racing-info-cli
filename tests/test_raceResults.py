from copy import deepcopy
import pytest
from src.driver.driver import Driver
from src.race.race import Race
from src.race.raceResults import RaceResults
from src.team.team import Team
from tests.dummy_data import DUMMY_DRIVER, DUMMY_DRIVER_TWO, DUMMY_RACE, DUMMY_TEAM, DUMMY_TEAM_TWO

# Fixtures

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

@pytest.fixture
def driver_fixture_two():
    return deepcopy(DUMMY_DRIVER_TWO)

@pytest.fixture
def race_fixture():
    return deepcopy(DUMMY_RACE)

@pytest.fixture
def team_fixture():
    return deepcopy(DUMMY_TEAM)

@pytest.fixture
def team_fixture_two():
    return deepcopy(DUMMY_TEAM_TWO)

# Test Cases

# TODO