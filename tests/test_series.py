from copy import deepcopy
import pytest
from src.series.series import Series
from tests.dummy_data import DUMMY_SERIES
from typing import Any

@pytest.fixture
def series_fixture():
    return deepcopy(DUMMY_SERIES)