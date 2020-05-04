import unittest
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription
from state_machines.game_states import StartingGameState, DraftCharacterCardsGameState
from test_machiavelli_game import TestMachiavelliGame

class GamePlayTest(TestMachiavelliGame):

    def test_add_player_to_game(self):
        game = MachiavelliGame()
        player1 = PlayerDescription('jeroen')
        game.registerPlayer(player1)
        player = game.getPlayer("jeroen")
        self.assertEqual(player.name, "jeroen")
    
    def test_positions_for_5_player_added(self):
        game = MachiavelliGame()
        game.registerPlayer(PlayerDescription('jeroen'))
        game.registerPlayer(PlayerDescription('robin'))
        game.registerPlayer(PlayerDescription('sander'))
        game.registerPlayer(PlayerDescription('martijn'))
        game.registerPlayer(PlayerDescription('casper'))

        player1 = game.getPlayer("jeroen")
        self.assertEqual(["jeroen",0],[player1.name, player1.position])

        player2 = game.getPlayer("robin")
        self.assertEqual(["robin",1],[player2.name, player2.position])

        player3 = game.getPlayer("sander")
        self.assertEqual(["sander",2],[player3.name, player3.position])
        
        player4 = game.getPlayer("martijn")
        self.assertEqual(["martijn",3],[player4.name, player4.position])

        player5 = game.getPlayer("casper")
        self.assertEqual(["casper",4],[player5.name, player5.position])

    def test_start_game_after_registration(self):
        game = MachiavelliGame()
        game.registerPlayer(PlayerDescription('jeroen'))
        game.registerPlayer(PlayerDescription('robin'))
        game.registerPlayer(PlayerDescription('sander'))
        game.registerPlayer(PlayerDescription('martijn'))
        game.registerPlayer(PlayerDescription('casper'))

        game.startGame()
        expectedState = DraftCharacterCardsGameState().__class__.__name__
        actualState = game.getState()
        self.assertEqual(expectedState,actualState)

if __name__ == '__main__':
    unittest.main()