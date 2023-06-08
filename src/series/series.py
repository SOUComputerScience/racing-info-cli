

class Series():
    """
    a class to represent a racing series
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name