from abc import ABC

class EngineInt(ABC):
    pass

class Engine(EngineInt):
    def __init__(self, engine: str):
        if not isinstance(engine, str):
            raise TypeError(f"{engine} must be of type str, not {type(engine)}")
        self.engine = engine

class FerrariEngine(EngineInt):
    def __init__(self):
        self.engine = "Ferrari"

class HondaRBPTEngine(EngineInt):
    def __init__(self):
        # I know, the name is far too long. I didn't choose it, Red Bull did
        self.engine = "Honda Red Bull Power Trains"

class MercedesEngine(EngineInt):
    def __init__(self):
        self.engine = "Mercedes"

class RenaultEngine(EngineInt):
    '''
    an engine manufactured by Renault.

    Fun Fact: Renault was one of the victims of WannaCry!
    https://www.nbcnews.com/business/autos/european-car-plants-halted-wannacry-ransomware-attack-n759496
    '''
    def __init__(self):
        self.engine = "Renault"