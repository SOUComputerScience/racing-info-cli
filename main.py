from src.championship.championship import Championship
from src.driver.driver import Driver
from src.engine.engine import *
from src.race.race import Race
from src.series.series import Series
from src.team.team import Team
from src.team.teamFactory import TeamFactory

def main():

    # instantiate the Formula One Series
    formula_one = Series("Formula One")

    # instantiate the 2023 Formula One Championship
    formula_one_2023 = Championship(series = formula_one, year = 2023)

    # create teams using TeamFactory

    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Alfa Romeo",
            country = "Switzerland",
            drivers = [
                Driver(surname = "Bottas", givenname = "Valtteri", nationality = "Finland"),
                Driver(surname = "Zhou", givenname = "Guanyu", nationality = "China", surname_first = True)
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamHondaRBPTEngine(
            name = "AlphaTauri",
            country = "Italy",
            drivers = [
                Driver(surname = "de Vries", givenname = "Nyck", nationality = "Netherlands"),
                Driver(surname = "Tsunoda", givenname = "Yuki", nationality = "Japan")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamRenaultEngine(
            name = "Alpine",
            country = "France",
            drivers = [
                # TODO add drivers
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Aston Martin",
            country = "United Kingdom",
            drivers = [
                # TODO add drivers
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Ferrari", # this is my second favorite team. They are terrible at strategy and there are multiple memes about how bad their strategy is
            country = "Italy",
            drivers = [
                # TODO add drivers
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Haas",
            country = "United States",
            drivers = [
                # TODO add drivers
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "McLaren",
            country = "United Kingdom",
            drivers = [
                Driver(surname = "Norris", givenname = "Lando", nationality = "United Kingdom"),
                Driver(surname = "Piastri", givenname = "Oscar", nationality = "Australia")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Mercedes", # this is my favorite team
            country = "Germany",
            drivers = [
                Driver(surname = "Hamilton", givenname = "Lewis", nationality = "United Kingdom"),
                Driver(surname = "Russell", givenname = "George", nationality = "United Kingdom")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamHondaRBPTEngine(
            name = "Red Bull", # you're not going to believe this, but Red Bull is actually a better team right now than Ferrari
            country = "Austria",
            drivers = [
                # TODO add drivers
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Williams",
            country = "United Kingdom",
            drivers = [
                # TODO add drivers
            ]
        )
    )

    for x in formula_one_2023.getTeamStandings():
        print(x)

if __name__ == "__main__":
    main()