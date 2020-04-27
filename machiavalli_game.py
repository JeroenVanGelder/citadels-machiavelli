from game_state_controller import GameStateController
from player.player import Player

class MachiavelliGame(object):

    def __init__(self):
        self.gameState = GameStateController()
        self.playerRegister = list()
        self.activePlayerPosition = 0

    def registerPlayer(self, playerDescription):
        if "registerPlayer" in self.gameState.get_allowed_actions():
            position = len(self.playerRegister)
            self.playerRegister.append(Player(playerDescription.name, position))
    
    def getPlayer(self, playerName):
        playerFound = None
        for player in self.playerRegister:
            if player.name == playerName:
                playerFound = player
        
        return playerFound

    def startGame(self):
        if "startGame" in self.gameState.get_allowed_actions():
            self.gameState.on_event("startGame")

    def getState(self):
        return self.gameState.get_game_state().__class__.__name__
    
    def draftCharacterCard(self, pickPlayerName, characterCard):
        if "draftCharacterCards" in self.gameState.get_allowed_actions():
            if self.getPlayer(pickPlayerName).position is self.activePlayerPosition:
                self.activePlayerPosition = self.activePlayerPosition + 1
                self.getPlayer(pickPlayerName).pick_character_card(characterCard)
            else:
                raise Exception('Not the current player')

    def getDraftingPlayer(self):
        playerFound = None
        for player in self.playerRegister:
            if player.position == self.activePlayerPosition:
                playerFound = player
        
        return playerFound