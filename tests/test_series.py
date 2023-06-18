from copy import deepcopy
import pytest
from src.series.series import Series
from tests.dummy_data import DUMMY_SERIES
from typing import Any

@pytest.fixture
def series_fixture():
    return deepcopy(DUMMY_SERIES)

def test___str__(series_fixture: Series):
    assert isinstance(series_fixture, Series)
    
    s = series_fixture.__str__()
    
    assert isinstance(s, str)
    assert s == "Dummy Series"