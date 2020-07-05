from cards.building_cards import BuildingCard
import random

class BuildingCardsController(object):

    def __init__(self):
        self.createAndSetNewCardRegister()

    def getAllBuildingCards(self):
        return self.buildingCardsRegister

    def getAllAvailableBuildingCards(self):
        availableCards = list()
        for buildingCard in self.buildingCardsRegister:
            if buildingCard.available:
                availableCards.append(buildingCard)
        return availableCards

    def getRandomBuildingCards(self, amount):
        buildingCards = list()
        for i in range(amount):
            rnd = random.randint(0, len(self.getAllAvailableBuildingCards())-1)
            card = self.getAllAvailableBuildingCards()[rnd]
            buildingCards.append(card)
            card.available = False
        return buildingCards

    def createAndSetNewCardRegister(self):
        self.buildingCardsRegister = list()
        tempBuildingCardsRegister = list()
        tempel = BuildingCard('tempel',1,'prediker','geen',3)
        wachttoren = BuildingCard('wachttoren',1,'condottiere','geen',3)
        taveerne = BuildingCard('taveerne',1,'koopman','geen',6)

        markt = BuildingCard('markt',2,'koopman','geen',4)
        kerk = BuildingCard('kerk',2,'prediker','geen',3)
        gildehuis = BuildingCard('gildehuis',2,'koopman','geen',3)
        kerker = BuildingCard('kerker',2,'condottiere','geen',3)
        hofDerWonderen = BuildingCard('hof der wonderen',2,'paars','special',1)

        toernooiveld = BuildingCard('toernooiveld',3,'condottiere','geen',3)
        jachtslot = BuildingCard('jachtslot',3,'koning','geen',5)
        abdij = BuildingCard('adbij',3,'prediker','geen',3)
        handelshuis = BuildingCard('handelshuis',3,'koopman','geen',3)
        verdedigingstoren = BuildingCard('verdedigingstoren', 3, 'paars','niet te vernietigen', 2)

        haven = BuildingCard('haven',4,'koopman','geen',3)
        slot = BuildingCard('slot',4,'koning','geen',4)

        kathedraal = BuildingCard('kathedraal',5,'prediker','geen',2)
        raadhuis = BuildingCard('raadhuis',5,'koopman','geen',2)
        paleis = BuildingCard('paleis',5,'koning','geen',2)
        vesting = BuildingCard('vesting',5,'condottiere','geen',2)

        laboratorium = BuildingCard('laboratorium',5,'paars','special',1)
        kerkhof = BuildingCard('kerkhof',5,'paars','special',1)
        observatorium = BuildingCard('observatorium',5,'paars','special',1)
        smederij = BuildingCard('smederij',5,'paars','special',1)
        schoolVoorMagiers = BuildingCard('school voor magiers',6,'paars','special',1)
        bibliotheek = BuildingCard('bibliotheek',6,'paars','special',1)
        drakenburcht = BuildingCard('drakenburcht',6,'paars','is 8 waard',1)
        universiteit = BuildingCard('universiteit',6,'paars','is 8 waard',1)

        tempBuildingCardsRegister.extend([
            tempel,wachttoren,taveerne,markt,kerk,gildehuis,
            kerker,toernooiveld,jachtslot,abdij,
            handelshuis,haven,slot,kathedraal,raadhuis,hofDerWonderen,
            verdedigingstoren,vesting, paleis,
            laboratorium, kerkhof, observatorium, smederij, schoolVoorMagiers, bibliotheek, drakenburcht, universiteit
        ])

        for card in tempBuildingCardsRegister:
            for i in range(card.totaal_in_spel):
                self.buildingCardsRegister.append(card)