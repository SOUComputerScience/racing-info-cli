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

    alfa_romeo = TeamFactory.createTeamFerrariEngine(
        name = "Alfa Romeo",
        country = "Switzerland",
        drivers = [bot, zho]
    )
    alphatauri = TeamFactory.createTeamHondaRBPTEngine(
        name = "AlphaTauri",
        country = "Italy",
        drivers = [dev, tsu]
    )
    alpine = TeamFactory.createTeamRenaultEngine(
        name = "Alpine",
        country = "France",
        drivers = [gas, oco]
    )
    aston_martin = TeamFactory.createTeamMercedesEngine(
        name = "Aston Martin",
        country = "United Kingdom",
        drivers = [alo, stroll]
    )
    ferrari = TeamFactory.createTeamFerrariEngine(
        name = "Ferrari", # this is my second favorite team. They are terrible at strategy and there are multiple memes about how bad their strategy is
        country = "Italy",
        drivers = [lec, sai]
    )
    haas = TeamFactory.createTeamFerrariEngine(
        name = "Haas",
        country = "United States",
        drivers = [hul, mag]
    )
    mclaren = TeamFactory.createTeamMercedesEngine(
        name = "McLaren",
        country = "United Kingdom",
        drivers = [nor, pia]
    )
    mercedes = TeamFactory.createTeamMercedesEngine(
        name = "Mercedes", # this is my favorite team
        country = "Germany",
        drivers = [ham, rus]
    )
    red_bull = TeamFactory.createTeamHondaRBPTEngine(
        name = "Red Bull", # you're not going to believe this, but Red Bull is actually a better team right now than Ferrari
        country = "Austria",
        drivers = [per, ver]
    )
    williams = TeamFactory.createTeamMercedesEngine(
        name = "Williams",
        country = "United Kingdom",
        drivers = [alb, sar]
    )

    # add teams to championship

    formula_one_2023.addTeamToChampionship(team = alfa_romeo)
    formula_one_2023.addTeamToChampionship(team = alphatauri)
    formula_one_2023.addTeamToChampionship(team = alpine)
    formula_one_2023.addTeamToChampionship(team = aston_martin)
    formula_one_2023.addTeamToChampionship(team = ferrari)
    formula_one_2023.addTeamToChampionship(team = haas)
    formula_one_2023.addTeamToChampionship(team = mclaren)
    formula_one_2023.addTeamToChampionship(team = mercedes)
    formula_one_2023.addTeamToChampionship(team = red_bull)
    formula_one_2023.addTeamToChampionship(team = williams)

    # add races and race results and print info

    # bahrain grand prix

    bahrain_gp = Race(
        name = "Bahrain Grand Prix",
        country = "Bahrain",
        city = "Sakhir",
        circuit = "Bahrain International Circuit"
    )
    print(bahrain_gp.__str__())
    rr = RaceResults(
        race = bahrain_gp,
        rankings = [
            ver, per, alo, sai, ham, stroll, rus, bot, gas, alb, tsu, sar, mag, dev, hul, zho, nor, oco, lec, pia
        ],
        fastestLap = zho
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # saudi arabian grand prix

    saudi_gp = Race(
        name = "Saudi Arabian Grand Prix",
        country = "Saudi Arabia",
        city = "Jeddah",
        circuit = "Jeddah Corniche Circuit"
    )
    print(saudi_gp.__str__())
    rr = RaceResults(
        race = saudi_gp,
        rankings = [
            per, ver, alo, rus, ham, sai, lec, oco, gas, mag, tsu, hul, zho, dev, pia, sar, nor, bot, alb, stroll
        ],
        fastestLap = ver
    )
    formula_one_2023.holdRace(rr)

    # australian grand prix

    australian_gp = Race(
        name = "Australian Grand Prix",
        country = "Australia",
        city = "Melbourne",
        circuit = "Albert Park Circuit"
    )
    print(australian_gp.__str__())
    rr = RaceResults(
        race = australian_gp,
        rankings = [ver, ham, alo, stroll, per, nor, hul, pia, zho, tsu, bot, sai, gas, oco, dev, sar, mag, rus, alb, lec],
        fastestLap = per
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # azerbaijan sprint race

    # manually update standings with azerbaijan sprint race results
    
    formula_one_2023.driver_standings[per] += 8
    formula_one_2023.driver_standings[lec] += 7
    formula_one_2023.driver_standings[ver] += 6
    formula_one_2023.driver_standings[rus] += 5
    formula_one_2023.driver_standings[sai] += 4
    formula_one_2023.driver_standings[alo] += 3
    formula_one_2023.driver_standings[ham] += 2
    formula_one_2023.driver_standings[stroll] += 1

    formula_one_2023.team_standings[aston_martin] += 4
    formula_one_2023.team_standings[ferrari] += 11
    formula_one_2023.team_standings[mercedes] += 7
    formula_one_2023.team_standings[red_bull] += 14

    # azerbaijan grand prix

    azerbaijan_gp = Race(
        name = "Azerbaijan Grand Prix",
        country = "Azerbaijan",
        city = "Baku",
        circuit = "Baku City Circuit"
    )
    print(azerbaijan_gp.__str__())
    rr = RaceResults(
        race = azerbaijan_gp,
        rankings = [per, ver, lec, alo, sai, ham, stroll, rus, nor, tsu, pia, alb, mag, gas, oco, sar, hul, bot, zho, dev],
        fastestLap = rus
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # miami grand prix

    miami_gp = Race(
        name = "Miami Grand Prix",
        country = "United States",
        city = "Miami",
        circuit = "Miami International Autodrome"
    )
    print(miami_gp.__str__())
    rr = RaceResults(
        race = miami_gp,
        rankings = [ver, per, alo, rus, sai, ham, lec, gas, oco, mag, tsu, stroll, bot, alb, hul, zho, nor, dev, pia, sar],
        fastestLap = ver
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # monaco grand prix

    monaco_gp = Race(
        name = "Monaco Grand Prix",
        country = "Monaco",
        city = "Monaco",
        circuit = "Circuit de Monaco"
    )
    print(monaco_gp.__str__())
    rr = RaceResults(
        race = monaco_gp,
        rankings = [ver, alo, oco, ham, rus, lec, gas, sai, nor, pia, bot, dev, zho, alb, tsu, per, hul, sar, mag, stroll],
        fastestLap = ham
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # spanish grand prix

    spanish_gp = Race(
        name = "Spanish Grand Prix",
        country = "Spain",
        city = "Barcelona",
        circuit = "Circuit de Barcelona-Catalunya"
    )
    print(spanish_gp.__str__())
    rr = RaceResults(
        race = spanish_gp,
        rankings = [ver, ham, rus, per, sai, stroll, alo, oco, zho, gas, lec, tsu, pia, dev, hul, alb, nor, mag, bot, sar],
        fastestLap = ver
    )
    formula_one_2023.holdRace(rr)
    print(rr.getPointsForDriver(driver = ver))

    # future races for the 2023 season

    canadian_gp = Race(
        name = "Canadian Grand Prix",
        country = "Canada",
        city = "Montreal",
        circuit = "Circuit Gilles Villeneuve"
    )

    austrian_gp = Race(
        name = "Austrian Grand Prix",
        country = "Austria",
        city = "Spielberg",
        circuit = "Red Bull Ring"
    )

    # TODO add the rest of the future races for 2023 (stretch goal)

    # print current standings to the console

    print("\nTeam Standings")
    for x in formula_one_2023.getTeamStandings():
        print(x)

    print("\nDriver Standings")
    for x in formula_one_2023.getDriverStandings():
        print(x)

if __name__ == "__main__":
    main()