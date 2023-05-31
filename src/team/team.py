from src.driver.driver import Driver

class Team():
    def __init__(self, name: str):
        self.name = name
        self.drivers = list(Driver)