import unittest, random
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription

class TestMachiavelliGame(unittest.TestCase):

    def getRandomCharacterCardName(self):
        allAvailableCards = self.game.getAvailableCharacterCards()
        randomCardPosition = random.randint(0, len(allAvailableCards))-1
        card = allAvailableCards[randomCardPosition].name
        return card

    def runFullRandomDraft(self):    
        jeroenCard = self.getRandomCharacterCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)
        robinCard = self.getRandomCharacterCardName()
        self.game.draftCharacterCard("robin", robinCard)
        sanderCard = self.getRandomCharacterCardName()
        self.game.draftCharacterCard("sander", sanderCard)
        martijnCard = self.getRandomCharacterCardName()
        self.game.draftCharacterCard("martijn", martijnCard)
        casperCard = self.getRandomCharacterCardName()
        self.game.draftCharacterCard("casper", casperCard)
        return {"jeroen": jeroenCard,
            "robin": robinCard, 
            "sander": sanderCard, 
            "martijn": martijnCard, 
            "casper": casperCard
        }

    def setStartedGameWith5Players(self):
        self.game = MachiavelliGame()
        self.game.registerPlayer(PlayerDescription('jeroen'))
        self.game.registerPlayer(PlayerDescription('robin'))
        self.game.registerPlayer(PlayerDescription('sander'))
        self.game.registerPlayer(PlayerDescription('martijn'))
        self.game.registerPlayer(PlayerDescription('casper'))

        self.game.startGame()

if __name__ == '__main__':
    unittest.main()