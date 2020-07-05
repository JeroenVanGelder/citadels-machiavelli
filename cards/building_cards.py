from dataclasses import dataclass, field
import typing

@dataclass
class BuildingCard(object):
    ''' Class to define the building cards '''
    name: str
    points: int
    eigenaar: str
    special: str
    totaal_in_spel: int
    available: bool = field(default=True, init=False)

    def __eq__(self, inputName):
        return inputName is self.name