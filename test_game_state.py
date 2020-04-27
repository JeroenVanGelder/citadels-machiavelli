import unittest
from game_state_controller import GameStateController
from player.playerDescriptions import PlayerDescription

class GameStateTest(unittest.TestCase):

    def test_if_game_is_started_game_starts(self):
        game = GameStateController()
        self.assertEqual("starting" ,game.state.__repr__())

    def test_allowed_registration_on_started_game(self):
        game = GameStateController()
        allowedActions = game.get_allowed_actions()
        self.assertIn("registerPlayer",allowedActions)

    # def test_add_player_to_game(self):
    #     game = GameStateController()
    #     player1 = PlayerDescription('jeroen')
    #     game.on_action("registerPlayer",player1)
    #     player = game.get_player("jeroen")
    #     self.assertEqual(player.name, "jeroen")

if __name__ == '__main__':
    unittest.main()