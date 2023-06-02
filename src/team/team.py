from src.driver.driver import Driver

class Team():
    def __init__(self, name: str, country: str):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be of type str, not {type(name)}")
        if not isinstance(country, str):
            raise TypeError(f"{country} must be of type str, not {type(country)}")
        
        self.name = name
        self.country = country

        self.drivers = list(Driver)

    def addDriverToTeam(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise TypeError(f"")
        
        if driver not in self.drivers:
            self.drivers.append(driver)

    def removeDriverFromTeam(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise TypeError(f"")
        
        if driver in self.drivers:
            self.drivers.remove(driver)