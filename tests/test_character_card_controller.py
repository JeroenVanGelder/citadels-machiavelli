import unittest
from cards.character_card_controller import CharacterCardController
from test_machiavelli_game import TestMachiavelliGame

class TestCharacterCardController(TestMachiavelliGame):

    def setUp(self):
        self.characterCardController = CharacterCardController()

    def test_ccc_is_present(self):
        pass

    def test_ccc_contains_9_character_cards(self):
        realAmountOfCC = len(self.characterCardController.getAllCharacterCards())
        self.assertEqual(8, realAmountOfCC)

    def test_ccc_exposes_2_cards_with_4_players(self):
        amountOfPlayers = 4
        self.characterCardController.exposeCharacterCards(amountOfPlayers)
        amountOfExposedCards = len(self.characterCardController.getExposedCharacterCards())
        self.assertEqual(2,amountOfExposedCards)

    def test_ccc_exposes_1_cards_with_5_players(self):
        amountOfPlayers = 4
        self.characterCardController.exposeCharacterCards(amountOfPlayers)
        amountOfExposedCards = len(self.characterCardController.getExposedCharacterCards())
        self.assertEqual(2,amountOfExposedCards)

    def test_ccc_does_not_expose_the_king(self):
        pass

if __name__ == '__main__':
    unittest.main()