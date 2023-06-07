import pytest
from src.driver.driver import Driver

@pytest.fixture
def driver_fixture():
    return Driver(
        surname = "Doe",
        givenname = "John",
        number = 0,
        nationality = "Internet",
        surname_first = False,
        suffix = "Jr."
    )

def test___str___(driver_fixture: Driver):
    d = driver_fixture
    s = d.__str__()

    assert isinstance(d, Driver)
    assert isinstance(s, str)

    assert s == "John DOE Jr. #0"

def test___str___surname_first(driver_fixture: Driver):
    d = driver_fixture
    d.surname_first = True
    s = d.__str__()

    assert isinstance(d, Driver)
    assert isinstance(s, str)

    assert s == "DOE John Jr. #0"