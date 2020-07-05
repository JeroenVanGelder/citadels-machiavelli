from player.player import Player

class PlayerController(object):

    def __init__(self):
        self.playerRegister = list()
        self.activeDraftPlayerPosition = 0
        self.activePlayingPlayerPosition = 0

    def registerPlayer(self, playerDescription):
        position = len(self.playerRegister)
        self.playerRegister.append(Player(playerDescription.name, position))

    def getPlayer(self, playerName):
        playerFound = None
        for player in self.playerRegister:
            if player.name == playerName:
                playerFound = player
        
        return playerFound

    def getAmountOfPlayers(self):
        return len(self.playerRegister)

    def getPlayerPosition(self, playerName):
        player = self.getPlayer(playerName)
        playerPosition = player.position
        return playerPosition

    def pickCharacterCard(self, playerName, characterCard):
        if self.isPlayerActiveDraftPlayer(playerName):
            player = self.getPlayer(playerName)
            player.pick_character_card(characterCard)
            self.activeDraftPlayerPosition = self.activeDraftPlayerPosition + 1
        else:
            raise Exception('Not the current player')

    def isPlayerActiveDraftPlayer(self,playerName):
        if self.getPlayerPosition(playerName) is self.activeDraftPlayerPosition:
            return True
        else:
            return False

    def getDraftingPlayer(self):
        playerFound = None
        for player in self.playerRegister:
            if player.position == self.activeDraftPlayerPosition:
                playerFound = player
        
        return playerFound

    def getActivePlayingPlayer(self):
        player = self.playerRegister[self.activePlayingPlayerPosition]
        return player

    def getAllPlayers(self):
        return self.playerRegister
    
    def getPlayerBuildingCardSelection(self, playerName):
        player = self.getPlayer(playerName)
        return player.getBuildingCardSelection()

    def pickBuildingCards(self, player, buildingCards):
        if player.pickedStartingResource is False:
            self.addPlayerBuildingCards(player, buildingCards)
            player.pickedStartingResource = True
        else:
            raise Exception("Player already picked a resource")

    def passTurn(self,player):
        self.activePlayingPlayerPosition += 1

    def pickGold(self, player):
        if player.pickedStartingResource is False:
            self.addPlayerGold(player, 2)
            player.pickedStartingResource = True
        else:
            raise Exception("Player already picked a resource")

    def allTurnsTaken(self):
        turnsTaken = self.activePlayingPlayerPosition
        amountOfPlayer = self.getAmountOfPlayers()
        if turnsTaken >= amountOfPlayer:
            return True
        return False

    def addPlayerGold(self, player, gold):
        player.gold = player.gold + gold

    def addPlayerBuildingCards(self, player, buildingCards):
        for buildingCard in buildingCards:
            player.addBuildingCardToHand(buildingCard)