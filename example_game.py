from cards.building_cards import buildingCardsList
from cards.character_cards import characterCardsList
from player.player import Player
import random


class MachiavelliGame(object):

    def __init__(self):
        print('Setting up Game')
        self.buildingCards = buildingCardsList
        self.characterCards = characterCardsList
        self.playersInGame = list()
        self.kingPosition = 1
        self.turn = 1
        print('Enter Players')

    def startGame(self):
        print('----------------\ngo\n----------------')
        self.draftCharacterCards()
        self.runPlayerTurns()
        print('----------------\nturn\playerRegistern----------------')

        self.draftCharacterCards()
        self.runPlayerTurns()
        print('----------------\nturn\n----------------')

        self.draftCharacterCards()
        self.runPlayerTurns()
        print('----------------\nturn\n----------------')

        self.draftCharacterCards()
        self.runPlayerTurns()
        print('----------------\nturn\n----------------')

    def registerPlayers(self, *playerList):
        position = 0
        for player in playerList:
            self.playersInGame.append(Player(player.name, position))
            position = position + 1

    def getPlayerPickPosition(self,player,kingPosition):
        currentPosition = player.position
        totalPositions = len(self.playersInGame)
        newPosition = currentPosition + (totalPositions - kingPosition)
        return newPosition % totalPositions

    def draftCharacterCards(self):
        print("\nPicking Character Cards")
        if self.turn > 1: 
            kingPosition = self.getKingPosition()
            for player in self.playersInGame:
                player.position=self.getPlayerPickPosition(player,kingPosition)
            self.playersInGame.sort(key=Player.getPlayerPosition)

        self.turn = self.turn + 1

        for player in self.playersInGame:
            rnd = random.randint(0, len(self.characterCards)-1)
            player.pick_character_card(self.characterCards[rnd])
            self.characterCards.pop(rnd)
            print(" ",player.name,"drafts", player.character.name)

        self.returnCharacterCards()

    def getKingPosition(self):
        kingPosition = 0
        for player in self.playersInGame:
            if player.character.name is 'koning':
                kingPosition = player.position
        return kingPosition

    def returnCharacterCards(self):
        for player in self.playersInGame:
            self.characterCards.append(player.character)

    def runPlayerTurns(self):
        print("\nRunning player turns")

        def getCharacterTurnPosition(plyr):
            return plyr.character.turn_position

        self.playersInGame.sort(key=getCharacterTurnPosition)

        for player in self.playersInGame:
            print(" turn for player", player.name, 'as', player.character.name if hasattr(player, 'character') else "none")
