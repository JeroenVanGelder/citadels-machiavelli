from game_state_controller import GameStateController
from cards.character_cards import CharacterCards
from cards.character_card_controller import CharacterCardController
from player.player import Player
from player.player_controller import PlayerController
import random


class MachiavelliGame(object):

    def __init__(self):
        self.gameState = GameStateController()
        self.playerController = PlayerController()
        self.characterCardsController = CharacterCardController()

    def registerPlayer(self, playerDescription):
        if "registerPlayer" in self.gameState.get_allowed_actions():
            self.playerController.registerPlayer(playerDescription)
    
    def getPlayer(self, playerName):
        playerFound = self.playerController.getPlayer(playerName)
        return playerFound

    def startGame(self):
        if "startGame" in self.gameState.get_allowed_actions():
            self.gameState.on_event("startGame")
            self.resetCharacterCards()
            self.exposeCharacterCards()

    def resetCharacterCards(self):
        self.characterCardsController.resetCharacterCards

    def exposeCharacterCards(self):
        amountOfPlayers = self.playerController.getAmountOfPlayers()
        self.characterCardsController.exposeCharacterCards(amountOfPlayers)

    def getState(self):
        return self.gameState.get_game_state().__class__.__name__
    
    def draftCharacterCard(self, pickPlayerName, characterCard):
        if "draftCharacterCards" in self.gameState.get_allowed_actions():
            if self.getCharacterCard(characterCard).available is True:
                self.playerController.pickCharacterCard(pickPlayerName, characterCard)
                self.getCharacterCard(characterCard).available = False
            else:
                raise Exception("Card not available")

            if self.playerController.getPlayerPosition(pickPlayerName) is len(self.playerController.playerRegister) -1:
                self.startCharacterTurns()

    def getDraftingPlayer(self):
        player = self.playerController.getDraftingPlayer()
        return player

    def getCharacterCard(self, characterCard):
        characterCard = self.characterCardsController.getCharacterCard(characterCard)
        return characterCard

    def getAllCharacterCards(self):
        return self.characterCardsController.getAllCharacterCards()

    def getAvailableCharacterCards(self):
        return self.characterCardsController.getAvailableCharacterCards()

    def startCharacterTurns(self):
        if "runCharacterTurns" in self.gameState.get_allowed_actions():
            self.gameState.on_event("runCharacterTurns")
            self.sortPlayersInCharacterOrder()

    def sortPlayersInCharacterOrder(self):
        def getCharacterTurnPosition(plyr):
            return self.getCharacterCard(plyr.character)
        self.playerController.playerRegister.sort(key=getCharacterTurnPosition)

    def getCurrentPlayer(self):
        player = self.playerController.getActivePlayingPlayer()
        return player

    def playerTakeAction(self, player, action):
        if "takeTurnAction" in self.gameState.get_allowed_actions():
            self.playerController.playerTakeAction(player, action)
            if self.playerController.allTurnsTaken():
                self.gameState.on_event("runCharacterCardsDraft")