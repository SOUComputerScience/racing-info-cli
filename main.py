from src.championship.championship import Championship
from src.driver.driver import Driver
from src.race.race import Race
from src.series.series import Series
from src.team.team import Team

def main():
    formula_one = Series("Formula One")

    formula_one_2023 = Championship(series = formula_one, year = 2023)

if __name__ == "__main__":
    main()