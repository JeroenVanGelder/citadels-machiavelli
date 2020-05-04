import unittest
from game_state_controller import GameStateController
from player.playerDescriptions import PlayerDescription
from test_machiavelli_game import TestMachiavelliGame

class GameStateTest(TestMachiavelliGame):

    def test_if_game_is_started_game_starts(self):
        game = GameStateController()
        self.assertEqual("starting" ,game.state.__repr__())

    def test_allowed_registration_on_started_game(self):
        game = GameStateController()
        allowedActions = game.get_allowed_actions()
        self.assertIn("registerPlayer",allowedActions)

if __name__ == '__main__':
    unittest.main()