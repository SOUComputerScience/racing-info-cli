

class Series():
    """
    a class to represent a racing series
    """
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be of type str, not {type(name)}")
        
        self.name = name

    def __str__(self) -> str:
        if not isinstance(self.name, str):
            raise TypeError(f"{self.name} must be of type str, not {type(self.name)}")

        return self.name