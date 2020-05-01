from game_state_controller import GameStateController
from cards.character_cards import characterCardsList
from player.player import Player
from player.player_controller import PlayerController
import random


class MachiavelliGame(object):

    def __init__(self):
        self.gameState = GameStateController()
        self.playerController = PlayerController()
        self.characterCards = characterCardsList

    def registerPlayer(self, playerDescription):
        if "registerPlayer" in self.gameState.get_allowed_actions():
            self.playerController.registerPlayer(playerDescription)
    
    def getPlayer(self, playerName):
        playerFound = self.playerController.getPlayer(playerName)
        return playerFound

    def startGame(self):
        if "startGame" in self.gameState.get_allowed_actions():
            self.gameState.on_event("startGame")
            self.resetCharacterCardS()
            self.exposeCharacterCards()

    def resetCharacterCardS(self):
        for card in self.characterCards:
            card.reset()

    def exposeCharacterCards(self):
        amountOfPlayers = self.playerController.getAmountOfPlayers()
        if amountOfPlayers is 4:
            openAmount = 2
        elif amountOfPlayers is 5:
            openAmount = 1
        else:
            openAmount = 0

        for x in range(0,openAmount):
            cardIsKing = True
            while cardIsKing:
                rnd = random.randint(0, len(self.characterCards)-1)
                if self.characterCards[rnd].name is not "koning":
                    cardIsKing = False
            self.characterCards[rnd].openCard()


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
        cardFound = None
        for card in self.characterCards:
            if card.name is characterCard:
                cardFound = card
        return cardFound

    def getAllCharacterCards(self):
        return self.characterCards

    def getAvailableCharacterCards(self):
        availableCards = list()
        for card in self.characterCards:
            if card.available is True:
                availableCards.append(card)
        return availableCards

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