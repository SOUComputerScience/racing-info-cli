from src.championship.championship import Championship
from src.driver.driver import Driver
from src.engine.engine import *
from src.race.race import Race
from src.race.raceResults import RaceResults
from src.series.series import Series
from src.team.team import Team
from src.team.teamFactory import TeamFactory

def main():

    # instantiate the Formula One Series
    formula_one = Series("Formula One")

    # instantiate the 2023 Formula One Championship
    formula_one_2023 = Championship(series = formula_one, year = 2023)

    # instantiate drivers

    alb = Driver(surname = "Albon", givenname = "Alexander", number = 23, nationality = "Thailand")
    alo = Driver(surname = "Alonso", givenname = "Fernando", number = 14, nationality = "Spain")
    bot = Driver(surname = "Bottas", givenname = "Valtteri", number = 77, nationality = "Finland")
    dev = Driver(surname = "de Vries", givenname = "Nyck", number = 21, nationality = "Netherlands")
    gas = Driver(surname = "Gasly", givenname = "Pierre", number = 10, nationality = "France")
    ham = Driver(surname = "Hamilton", givenname = "Lewis", number = 44, nationality = "United Kingdom")
    hul = Driver(surname = "Hülkenberg", givenname = "Nico", number = 27, nationality = "Germany")
    lec = Driver(surname = "Leclerc", givenname = "Charles", number = 16, nationality = "Monaco")
    mag = Driver(surname = "Magnussen", givenname = "Kevin", number = 20, nationality = "Denmark")
    nor = Driver(surname = "Norris", givenname = "Lando", number = 4, nationality = "United Kingdom")
    oco = Driver(surname = "Ocon", givenname = "Esteban", number = 31, nationality = "France")
    per = Driver(surname = "Pérez", givenname = "Sergio", number = 11, nationality = "Mexico")
    pia = Driver(surname = "Piastri", givenname = "Oscar", number = 81, nationality = "Australia")
    rus = Driver(surname = "Russell", givenname = "George", number = 63, nationality = "United Kingdom")
    sai = Driver(surname = "Sainz", suffix = "Jr.", givenname = "Carlos", number = 55, nationality = "Spain")
    sar = Driver(surname = "Sargeant", givenname = "Logan", number = 2, nationality = "United States")
    stroll = Driver(surname = "Stroll", givenname = "Lance", number = 18, nationality = "Canada") # str is a reserved word
    tsu = Driver(surname = "Tsunoda", givenname = "Yuki", number = 22, nationality = "Japan")
    ver = Driver(surname = "Verstappen", givenname = "Max", number = 1, nationality = "Netherlands")
    zho = Driver(surname = "Zhou", givenname = "Guanyu", number = 24, nationality = "China", surname_first = True)

    # create teams using TeamFactory

    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Alfa Romeo",
            country = "Switzerland",
            drivers = [bot, zho]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamHondaRBPTEngine(
            name = "AlphaTauri",
            country = "Italy",
            drivers = [dev, tsu]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamRenaultEngine(
            name = "Alpine",
            country = "France",
            drivers = [gas, oco]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Aston Martin",
            country = "United Kingdom",
            drivers = [alo, stroll]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Ferrari", # this is my second favorite team. They are terrible at strategy and there are multiple memes about how bad their strategy is
            country = "Italy",
            drivers = [lec, sai]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamFerrariEngine(
            name = "Haas",
            country = "United States",
            drivers = [hul, mag]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "McLaren",
            country = "United Kingdom",
            drivers = [nor, pia]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Mercedes", # this is my favorite team
            country = "Germany",
            drivers = [ham, rus]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamHondaRBPTEngine(
            name = "Red Bull", # you're not going to believe this, but Red Bull is actually a better team right now than Ferrari
            country = "Austria",
            drivers = [per, ver]
        )
    )
    formula_one_2023.addTeamToChampionship(
        TeamFactory.createTeamMercedesEngine(
            name = "Williams",
            country = "United Kingdom",
            drivers = [alb, sar]
        )
    )

    # add races and race results and print info

    # bahrain grand prix
    bahrain_gp = Race(
        name = "Bahrain Grand Prix",
        country = "Bahrain",
        city = "Sakhir",
        circuit = "Bahrain International Circuit"
    )
    print(bahrain_gp.__str__())
    formula_one_2023.holdRace(
        RaceResults(
            race = bahrain_gp,
            rankings = [
                ver, per, alo, sai, ham, stroll, rus, bot, gas, alb, tsu, sar, mag, dev, hul, zho, nor, oco, lec, pia
            ],
            fastestLap = zho
        )
    )

    # TODO: saudi arabian grand prix

    # TODO: australian grand prix

    # TODO: azerbaijan grand prix

    # TODO: saudi arabian grand prix

    # TODO: miami grand prix

    # TODO: monaco grand prix

    # TODO: spanish grand prix

    # print standings to the console

    print("\nTeam Standings")
    for x in formula_one_2023.getTeamStandings():
        print(x)

    print("\nDriver Standings")
    for x in formula_one_2023.getDriverStandings():
        print(x)

if __name__ == "__main__":
    main()