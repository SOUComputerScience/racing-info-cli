

class Race():
    """
    TODO
    """
    def __init__(self, name: str, country: str, city: str):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be of type str, not {type(name)}")
        if not isinstance(country, str):
            raise TypeError(f"{country} must be of type str, not {type(country)}")
        if not isinstance(city, str):
            raise TypeError(f"{city} must be of type str, not {type(city)}")

        self.name = name
        self.country = country
        self.city = city

    def __str__(self) -> str:
        return f"{self.name} Grand Prix ({self.city}, {self.country})"