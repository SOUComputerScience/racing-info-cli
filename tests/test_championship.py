from copy import deepcopy
import pytest
from src.championship.championship import Championship
from src.driver.driver import Driver
from src.race.race import Race
from src.race.raceResults import RaceResults
from src.series.series import Series
from src.team.team import Team
from tests.dummy_data import * # TODO edit this later to only import used dummy vars 
from typing import Any, List

# fixtures

@pytest.fixture
def championship_fixture():
    return deepcopy(DUMMY_CHAMPIONSHIP)

# TODO test cases