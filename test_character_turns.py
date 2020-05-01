import unittest, random
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription



class CharacterCardDraftTest(unittest.TestCase):

    def setUp(self):
        self.game = MachiavelliGame()
        self.game.registerPlayer(PlayerDescription('jeroen'))
        self.game.registerPlayer(PlayerDescription('robin'))
        self.game.registerPlayer(PlayerDescription('sander'))
        self.game.registerPlayer(PlayerDescription('martijn'))
        self.game.registerPlayer(PlayerDescription('casper'))

        self.game.startGame()
        self.draftedCards = self.runFullRandomDraft()

    def test_game_is_ready_for_character_turns(self):
        gamestate = self.game.getState()
        turnGameState = "RunCharacterTurnsGameState"
        self.assertEqual(turnGameState, gamestate)

    def test_game_sorted_players_in_character_order(self):
        firstPlayerCharacter = self.game.getCharacterCard(self.game.playerController.playerRegister[0].character).turn_position
        secondPlayerCharacter = self.game.getCharacterCard(self.game.playerController.playerRegister[1].character).turn_position
        thirdPlayerCharacter = self.game.getCharacterCard(self.game.playerController.playerRegister[2].character).turn_position
        fourthPlayerCharacter = self.game.getCharacterCard(self.game.playerController.playerRegister[3].character).turn_position
        fifthPlayerCharacter = self.game.getCharacterCard(self.game.playerController.playerRegister[4].character).turn_position
        
        self.assertLess(firstPlayerCharacter, secondPlayerCharacter)
        self.assertLess(secondPlayerCharacter, thirdPlayerCharacter)
        self.assertLess(thirdPlayerCharacter, fourthPlayerCharacter)
        self.assertLess(fourthPlayerCharacter, fifthPlayerCharacter)

    def test_game_knows_active_player_at_start_of_turns(self):
        registerTurn = self.game.playerController.playerRegister[0]
        askedTurn = self.game.getCurrentPlayer()
        self.assertEqual(registerTurn, askedTurn)
        
    def test_players_can_take_their_turns(self):
        player = self.game.getCurrentPlayer()
        action = "pick card"
        self.game.playerTakeAction(player, action)
        pass

    def test_active_player_changes_after_player_pass_turn(self):
        player = self.game.getCurrentPlayer()
        action = "pass_turn"
        self.game.playerTakeAction(player, action)
        correctPlayerTurn = self.game.playerController.playerRegister[1]
        actualPlayerTurn = self.game.getCurrentPlayer()
        self.assertEqual(correctPlayerTurn, actualPlayerTurn)

    def test_not_active_player_cant_take_turn(self):
        player = self.game.playerController.playerRegister[1]
        action = "take_turn"
        with self.assertRaises(Exception):
            self.game.playerTakeAction(player, action)

    @unittest.skip("unimplemented")
    def test_game_goes_to_draft_when_all_players_have_taken_their_turn(self):
        pass

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

if __name__ == '__main__':
    unittest.main()