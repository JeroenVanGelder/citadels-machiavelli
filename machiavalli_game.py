from game_state_controller import GameStateController
from cards.character_cards import CharacterCards
from cards.character_card_controller import CharacterCardController
from player.player import Player
from player.player_controller import PlayerController
from cards.buildingCardsController import BuildingCardsController
import random

class MachiavelliGame(object):

    def __init__(self):
        self.gameState = GameStateController()
        self.playerController = PlayerController()
        self.characterCardsController = CharacterCardController()
        self.buildingCardsController = BuildingCardsController()

    def registerPlayer(self, playerDescription):
        if "registerPlayer" in self.gameState.get_allowed_actions():
            self.playerController.registerPlayer(playerDescription)
            player = self.getPlayer(playerDescription.name)
            startingCards = self.buildingCardsController.getRandomBuildingCards(4)
            self.playerController.addPlayerBuildingCards(player, startingCards)
    
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

    def getAllPlayers(self):
        return self.playerController.getAllPlayers()

    ############################################################
    ############    player actions      ########################
    ############################################################

    def playerTakeAction(self, playerName, actionName, **kwargs):
        if "takeTurnAction" in self.gameState.get_allowed_actions():
            player = self.getPlayer(playerName)
            action = self.getPlayerAction(actionName)
            self.executePlayerAction(player, action, **kwargs)
            if self.playerController.allTurnsTaken():
                self.gameState.on_event("runCharacterCardsDraft")

    def executePlayerAction(self, player, action, **kwargs): 
        if player is self.playerController.getActivePlayingPlayer():
            try:
                if any(kwargs):
                    action(player, **kwargs)
                else:
                    action(player)
            except:
                raise Exception(action, "is not a known or allowed action")
        else:
            raise Exception(player.name, 'is not the current player', self.getActivePlayingPlayer().name)

    def getPlayerAction(self, actionName):
        return {
            'pick_gold': self.pickGold,
            'pass_turn': self.passTurn,
            'pick_cards': self.pickBuildingCards,
            'build_card': self.buildABuildingCard
            }.get(actionName)

    def buildABuildingCard(self, player, **kwargs):
        buildingCardName = kwargs['buildingCard']
        try:
            buildingCard = { card.name : card for card in player.getBuildingCardsInHand()}[buildingCardName]
            player.buildABuildingCard(buildingCard)
        except:
            print(player.getBuildingCardsInHand())
            raise Exception(buildingCardName, "is not a card ", player.name, "has")


    def pickBuildingCards(self, player):
        randomBuildingCards = self.buildingCardsController.getRandomBuildingCards(2)
        player.setBuildingCardSelection(randomBuildingCards)
        pass
    
    def playerSelectBuildingCard(self, playerName, card):
        player = self.getPlayer(playerName)
        if "takeTurnAction" in self.gameState.get_allowed_actions():
            if player is self.playerController.getActivePlayingPlayer():
                if card in player.getBuildingCardSelection():
                    player.selectBuildingCard(card)
        

    def passTurn(self,player):
        self.playerController.passTurn(player)

    def pickGold(self, player):
        if player.pickedStartingResource is False:
            self.playerController.pickGold(player)
        else:
            raise Exception("Player already picked a resource")

    ############################################################
    ############    Building cards      ########################
    ############################################################


    def getAllBuildingCards(self):
        buildingCards = self.buildingCardsController.getAllBuildingCards()
        return buildingCards

    def getAllAvailableBuildingCards(self):
        buildingCards = self.buildingCardsController.getAllAvailableBuildingCards()
        return buildingCards

    def getPlayerBuildingCardSelection(self, playerName):
        return self.playerController.getPlayerBuildingCardSelection(playerName)
        