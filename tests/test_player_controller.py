import unittest
from player.player_controller import PlayerController
from tests.test_machiavelli_game import TestMachiavelliGame

class TestPlayerController(TestMachiavelliGame):

    def test_controller_exists(self):
        playerController = PlayerController()
        self.assertNotEqual(None, playerController)

if __name__ == '__main__':
    unittest.main()