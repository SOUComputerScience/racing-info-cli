from copy import deepcopy
import pytest
from src.driver.driver import Driver
from tests.dummy_data import DUMMY_DRIVER

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

def test___str___(driver_fixture: Driver):

    assert isinstance(driver_fixture, Driver)

    s = driver_fixture.__str__()
    assert isinstance(s, str)

    assert s == "John DOE Jr. #0"

def test___str___surname_first(driver_fixture: Driver):
    
    assert isinstance(driver_fixture, Driver)

    driver_fixture.surname_first = True
    assert isinstance(driver_fixture, Driver)

    s = driver_fixture.__str__()
    assert isinstance(s, str)

    assert s == "DOE John Jr. #0"