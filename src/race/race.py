

class Race():
    def __init__(self, name: str, country: str, city: str):
        if not isinstance(name, str):
            raise TypeError(f"")
        if not isinstance(country, str):
            raise TypeError(f"")
        if not isinstance(city, str):
            raise TypeError(f"")

        self.name = name
        self.country = country
        self.city = city