from copy import deepcopy
import pytest
from src.engine.engine import Engine
from tests.dummy_data import DUMMY_ENGINE

# Fixtures

@pytest.fixture
def engine_fixture():
    return deepcopy(DUMMY_ENGINE)

# Test Cases

def test___str__(engine_fixture: Engine):
    assert isinstance(engine_fixture, Engine)
    
    s = engine_fixture.__str__()
    
    assert isinstance(s, str)
    assert s == "Dummy Engine"