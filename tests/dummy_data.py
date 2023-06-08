from src.championship.championship import Championship
from src.driver.driver import Driver
from src.engine.engine import Engine
from src.race.race import Race
from src.series.series import Series
from src.team.team import Team

DUMMY_DRIVER = Driver(
    surname = "Doe",
    givenname = "John",
    number = 0,
    nationality = "Internet",
    surname_first = False,
    suffix = "Jr."
)

DUMMY_DRIVER_TWO = Driver(
    surname = "",
    givenname = "",
    number = -1,
    nationality = "",
    surname_first = False,
    suffix = None
)

DUMMY_ENGINE = Engine(engine = "Dummy Engine")

DUMMY_RACE = Race(
    name = "Dummy Race",
    country = "Internet",
    city = "Internet City",
    circuit = "Internet Circuit"
)

DUMMY_SERIES = Series(
    name = "Dummy Series"
)

DUMMY_CHAMPIONSHIP = Championship(
    series = DUMMY_SERIES,
    year = 0
)

DUMMY_TEAM = Team(
    name = "Dummy Team",
    engine = DUMMY_ENGINE,
    country = "Internet",
    drivers = []
)