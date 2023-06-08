

class Race():
    """
    TODO
    """
    def __init__(self, name: str, country: str, city: str, circuit: str):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be of type str, not {type(name)}")
        if not isinstance(country, str):
            raise TypeError(f"{country} must be of type str, not {type(country)}")
        if not isinstance(city, str):
            raise TypeError(f"{city} must be of type str, not {type(city)}")
        if not isinstance(circuit, str):
            raise TypeError(f"{circuit} must be of type str, not {type(circuit)}")

        self.name = name
        self.country = country
        self.city = city
        self.circuit = circuit

    def __str__(self) -> str:
        return f"{self.name} ({self.circuit} in {self.city}, {self.country})"