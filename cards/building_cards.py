from dataclasses import dataclass, field
import typing

@dataclass
class BuildingCards(object):
    ''' Class to define the building cards '''
    name: str
    points: int
    eigenaar: str
    special: str
    totaal_in_spel: int

buildingCardsList = []

tempel = BuildingCards('tempel',1,'prediker','geen',6)
wachttoren = BuildingCards('wachttoren',1,'condottiere','geen',6)
taveerne = BuildingCards('taveerne',1,'koopman','geen',6)
markt = BuildingCards('markt',2,'koopman','geen',5)
kerk = BuildingCards('kerk',2,'prediker','geen',5)
gildehuis = BuildingCards('gildehuis',2,'koopman','geen',5)
kerker = BuildingCards('kerker',2,'condottiere','geen',5)
toernooiveld = BuildingCards('toernooiveld',3,'condottiere','geen',4)
jachtslot = BuildingCards('jachtslot',3,'koning','geen',4)
abdij = BuildingCards('adbij',3,'prediker','geen',4)
handelshuis = BuildingCards('handelshuis',3,'koopman','geen',4)
haven = BuildingCards('haven',4,'koopman','geen',3)
slot = BuildingCards('slot',4,'koning','geen',3)
kathedraal = BuildingCards('kathedraal',5,'prediker','geen',2)
raadhuis = BuildingCards('raadhuis',5,'koopman','geen',2)

buildingCardsList.extend([
    tempel,wachttoren,taveerne,markt,kerk,gildehuis,
    kerker,toernooiveld,jachtslot,abdij,
    handelshuis,haven,slot,kathedraal,raadhuis
])