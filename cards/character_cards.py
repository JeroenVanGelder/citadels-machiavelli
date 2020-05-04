from dataclasses import dataclass, field
import typing

@dataclass(order=True)
class CharacterCards(object):
    ''' Class for the character cards'''
    name: str = field(compare=False)
    turn_position: int = field(compare=True)
    available: bool = field(compare=False, default=True, init=False)
    open: bool = field(compare=False, default=False, init=False)
    power: str = field(compare=False)

    def openCard(self):
        self.open = True
        self.available = False

    def reset(self):
        self.open = False
        self.available = True