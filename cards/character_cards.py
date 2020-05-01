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

characterCardsList = []

moordenaar = CharacterCards('moordenaar',1,'kill a guy')
dief = CharacterCards('dief',2,'Steal stuff')
magier = CharacterCards('magier',3,'Swap hands')
koning = CharacterCards('koning',4,'Select First Card')
prediker = CharacterCards('prediker',5,'Imune to condottiere')
koopman = CharacterCards('koopman',6,'extra doekoe')
bouwmeester = CharacterCards('bouwmeester',7,'twee kaarten en drie bouwen')
condottiere = CharacterCards('condottiere',8,'mol n gebouw')

characterCardsList.extend([moordenaar, dief, magier, koning, prediker, koopman, bouwmeester, condottiere])