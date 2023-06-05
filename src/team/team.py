from src.driver.driver import Driver
from src.engine.engine import *
from typing import List

class Team():
    """
    a class to represent a racing team.
    """
    def __init__(self, name: str, engine: EngineInt, country: str, drivers: List[Driver]):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be of type str, not {type(name)}")
        if not isinstance(engine, EngineInt):
            raise TypeError(f"{engine} must be of type EngineInt or its subclasses, not {type(engine)}")
        if not isinstance(country, str):
            raise TypeError(f"{country} must be of type str, not {type(country)}")
        if not isinstance(drivers, list):
            raise TypeError(f"{drivers} must be of type list, not {type(drivers)}")
        
        self.name = name
        self.engine = engine
        self.country = country
        self.drivers = list()

        # because the addDriverToTeam() method does type checking internally, we don't need to create an extra for loop to check each item in the list of prospective drivers. this saves processing time and memory!
        for driver in drivers:
            self.addDriverToTeam(driver = driver)

    def addDriverToTeam(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise TypeError(f"{driver} must be of type Driver, not {type(driver)}")
        
        if driver not in self.drivers:
            self.drivers.append(driver)

    def removeDriverFromTeam(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise TypeError(f"")
        
        if driver in self.drivers:
            self.drivers.remove(driver)