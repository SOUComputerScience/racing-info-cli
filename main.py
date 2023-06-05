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
                Driver(surname = "Bottas", givenname = "Valtteri", number = 77, nationality = "Finland"),
                Driver(surname = "Zhou", givenname = "Guanyu", number = 24, nationality = "China", surname_first = True)
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamHondaRBPTEngine(
            name = "AlphaTauri",
            country = "Italy",
            drivers = [
                Driver(surname = "de Vries", givenname = "Nyck", number = 21, nationality = "Netherlands"),
                Driver(surname = "Tsunoda", givenname = "Yuki", number = 22, nationality = "Japan")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamRenaultEngine(
            name = "Alpine",
            country = "France",
            drivers = [
                Driver(surname = "Gasly", givenname = "Pierre", number = 10, nationality = "France"),
                Driver(surname = "Ocon", givenname = "Esteban", number = 31, nationality = "France")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Aston Martin",
            country = "United Kingdom",
            drivers = [
               Driver(surname = "Alonso", givenname = "Fernando", number = 14, nationality = "Spain"),
               Driver(surname = "Stroll", givenname = "Lance", number = 18, nationality = "Canada")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Ferrari", # this is my second favorite team. They are terrible at strategy and there are multiple memes about how bad their strategy is
            country = "Italy",
            drivers = [
                Driver(surname = "Leclerc", givenname = "Charles", number = 16, nationality = "Monaco"),
                Driver(surname = "Sainz", suffix = "Jr.", givenname = "Carlos", number = 55, nationality = "Spain")
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
                Driver(surname = "Norris", givenname = "Lando", number = 4, nationality = "United Kingdom"),
                Driver(surname = "Piastri", givenname = "Oscar", number = 81, nationality = "Australia")
            ]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Mercedes", # this is my favorite team
            country = "Germany",
            drivers = [
                Driver(surname = "Hamilton", givenname = "Lewis", number = 44, nationality = "United Kingdom"),
                Driver(surname = "Russell", givenname = "George", number = 63, nationality = "United Kingdom")
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

    # print standings to the console

    print("\nTeam Standings")
    for x in formula_one_2023.getTeamStandings():
        print(x)

    print("\nDriver Standings")
    for x in formula_one_2023.getDriverStandings():
        print(x)

if __name__ == "__main__":
    main()