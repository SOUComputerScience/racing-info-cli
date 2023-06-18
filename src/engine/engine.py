from abc import ABC

class EngineInt(ABC):
    """
    an interface for engines
    """
    def __str__(self) -> str:
        pass

class Engine(EngineInt):
    """
    TODO
    """
    def __init__(self, engine: str):
        if not isinstance(engine, str):
            raise TypeError(f"{engine} must be of type str, not {type(engine)}")
        self.engine = engine

    def __str__(self) -> str:
        return f"{self.engine} Engine"

class FerrariEngine(EngineInt):
    """
    a class to represent an Engine built by Ferrari.
    """
    def __init__(self):
        self.engine = "Ferrari"

    def __str__(self) -> str:
        return f"{self.engine} Engine"

class HondaRBPTEngine(EngineInt):
    """
    a class to represent an Engine built by Honda Red Bull Power Trains.
    """
    def __init__(self):
        # I know, the name is far too long. 
        # I didn't choose it, Red Bull did
        self.engine = "Honda Red Bull Power Trains"

class MercedesEngine(EngineInt):
    """
    a class to represent an engine built by Mercedes.
    """
    def __init__(self):
        self.engine = "Mercedes"

    def __str__(self) -> str:
        return f"{self.engine} Engine"

class RenaultEngine(EngineInt):
    '''
    a class to represent an engine built by Renault.

    Fun Fact: Renault was one of the victims of WannaCry!
    https://www.nbcnews.com/business/autos/european-car-plants-halted-wannacry-ransomware-attack-n759496
    '''
    def __init__(self):
        self.engine = "Renault"

    def __str__(self) -> str:
        return f"{self.engine} Engine"