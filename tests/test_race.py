from copy import deepcopy
import pytest
from src.race.race import Race
from tests.dummy_data import DUMMY_RACE

# Fixtures

@pytest.fixture
def race_fixture():
    return deepcopy(DUMMY_RACE)

# Test Cases

def test___str__(race_fixture: Race):
    assert isinstance(race_fixture, Race)
    
    s = race_fixture.__str__()
    
    assert isinstance(s, str)
    assert s == f"Dummy Race (Internet Circuit in Internet City, Internet)"