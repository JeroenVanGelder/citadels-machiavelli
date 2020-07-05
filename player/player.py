# player.py

class Player(object):
    """
    A player defines a player and their current state
    """
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.gold = 2 
        self.pickedStartingResource = False
        self.buildingCardsInHand = list()
        self.buildingCardSelection = list()
        self.buildingCardsInPlay = list()

    def pick_character_card(self, character):
        self.character = character
    
    def getPlayerPosition(self):
        return self.position
    
    def getBuildingCardsInHand(self):
        return self.buildingCardsInHand

    def addBuildingCardToHand(self, buildingCard):
        self.buildingCardsInHand.append(buildingCard)

    def buildABuildingCard(self, buildingCard):
        self.buildingCardsInPlay.append(buildingCard)

    def getBuildingCardSelection(self):
        return self.buildingCardSelection
    
    def setBuildingCardSelection(self, buildingCards):
        self.buildingCardSelection.clear()
        for buildingCard in buildingCards:
            self.buildingCardSelection.append(buildingCard)
    
    def selectBuildingCard(self, buildingCard):
        self.buildingCardsInHand.append(buildingCard)
        self.buildingCardSelection.clear()

    def getAllBuildingsInPlay(self):
        return self.buildingCardsInPlay

    def getGold(self):
        return self.gold