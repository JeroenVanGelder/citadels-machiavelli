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
    
    def playerTakeAction(self, player, action):
        if player is self.getActivePlayingPlayer():
            if action is "pass_turn":
                self.activePlayingPlayerPosition += 1
            else:
                pass
        else:
            raise Exception(player.name, 'is not the current player', self.getActivePlayingPlayer().name)

    def allTurnsTaken(self):
        turnsTaken = self.activePlayingPlayerPosition
        amountOfPlayer = self.getAmountOfPlayers()
        if turnsTaken >= amountOfPlayer:
            return True
        return False