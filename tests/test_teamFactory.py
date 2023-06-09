from copy import deepcopy
import pytest
from src.engine.engine import *
from src.team.team import Team
from src.team.teamFactory import *
from tests.dummy_data import DUMMY_DRIVER, DUMMY_ENGINE, DUMMY_TEAM
from typing import Any

# Fixtures

@pytest.fixture
def driver_fixture():
    return deepcopy(DUMMY_DRIVER)

@pytest.fixture
def engine_fixture():
    return deepcopy(DUMMY_ENGINE)

# Helper Method

def verify_teams(expected: Team, actual: Any):
    assert type(expected) == type(actual) == Team

    assert expected.name == actual.name

    assert type(expected.engine) == type(actual.engine) and issubclass(type(expected.engine), EngineInt)
    assert expected.engine == actual.engine

    assert expected.country == actual.country
    
    assert type(expected.drivers) == type(actual.drivers) == list
    assert len(expected.drivers) == len(actual.drivers)
    for i in range(len(expected.drivers)):
        assert expected.drivers[i] == actual.drivers[i]

# Test Cases

def test_createTeam(engine_fixture: Engine):
    assert isinstance(engine_fixture, Engine)

    t = TeamFactory.createTeam(
        name = "Foo",
        engine = engine_fixture,
        country = "Foo",
        drivers = [DUMMY_DRIVER]
    )
    
    assert isinstance(t, Team)

    verify_teams(
        expected = Team(name = "Foo", engine = engine_fixture, country = "Foo", drivers = [DUMMY_DRIVER]), actual = t
    )

def test_createTeamFerrariEngine():
    ferrari = FerrariEngine()

    t = TeamFactory.createTeam(
        name = "Foo",
        engine = ferrari,
        country = "Foo",
        drivers = [DUMMY_DRIVER]
    )
    
    assert isinstance(t, Team)

    verify_teams(
        expected = Team(name = "Foo", engine = ferrari, country = "Foo", drivers = [DUMMY_DRIVER]), actual = t
    )

def test_createTeamHondaRBPTEngine():
    hondarbpt = HondaRBPTEngine()

    t = TeamFactory.createTeam(
        name = "Foo",
        engine = hondarbpt,
        country = "Foo",
        drivers = [DUMMY_DRIVER]
    )
    
    assert isinstance(t, Team)

    verify_teams(
        expected = Team(name = "Foo", engine = hondarbpt, country = "Foo", drivers = [DUMMY_DRIVER]), actual = t
    )

def test_createTeamMercedesEngine():
    mercedes = MercedesEngine()

    t = TeamFactory.createTeam(
        name = "Foo",
        engine = mercedes,
        country = "Foo",
        drivers = [DUMMY_DRIVER]
    )
    
    assert isinstance(t, Team)

    verify_teams(
        expected = Team(name = "Foo", engine = mercedes, country = "Foo", drivers = [DUMMY_DRIVER]), actual = t
    )

def test_createTeamRenaultEngine():
    renault = RenaultEngine()

    t = TeamFactory.createTeam(
        name = "Foo",
        engine = renault,
        country = "Foo",
        drivers = [DUMMY_DRIVER]
    )
    
    assert isinstance(t, Team)

    verify_teams(
        expected = Team(name = "Foo", engine = renault, country = "Foo", drivers = [DUMMY_DRIVER]), actual = t
    )