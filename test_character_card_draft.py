import unittest
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

    def test_draft_first_character_card(self):
        self.game.draftCharacterCard("jeroen","koning")

    def test_get_drafting_player(self):
        draftingPlayer = self.game.getDraftingPlayer()
        self.assertEqual('jeroen',draftingPlayer.name)

    def test_get_drafting_player_after_one_pick(self):
        self.game.draftCharacterCard("jeroen","koning")
        draftingPlayer = self.game.getDraftingPlayer()
        self.assertEqual('robin',draftingPlayer.name)

    def test_draft_when_not_active_player(self):
        with self.assertRaises(Exception):
             self.game.draftCharacterCard("robin","koning")

    def test_draft_when_not_active_player_after_pick(self):
        self.game.draftCharacterCard("jeroen","koning")
        with self.assertRaises(Exception):
             self.game.draftCharacterCard("jeroen","koning")

    def test_player_is_character_after_draft_pick(self):
        self.game.draftCharacterCard("jeroen","koning")
        self.assertEqual("koning",self.game.getPlayer("jeroen").character)
    
    @unittest.skip("skipping")
    def test_available_cards_one_less_after_draft_pick(self):
    
#Test if the game handles the character cards correctly during the draft process

#test if the game continues correctly when done drafter


if __name__ == '__main__':
    unittest.main()