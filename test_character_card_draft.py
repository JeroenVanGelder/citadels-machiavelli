import unittest, random
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription
from test_machiavelli_game import TestMachiavelliGame

class CharacterCardDraftTest(TestMachiavelliGame):

    def setUp(self):
        self.game = MachiavelliGame()
        self.game.registerPlayer(PlayerDescription('jeroen'))
        self.game.registerPlayer(PlayerDescription('robin'))
        self.game.registerPlayer(PlayerDescription('sander'))
        self.game.registerPlayer(PlayerDescription('martijn'))
        self.game.registerPlayer(PlayerDescription('casper'))

        self.game.startGame()

    def getRandomCardName(self):
        allAvailableCards = self.game.getAvailableCharacterCards()
        randomCardPosition = random.randint(0, len(allAvailableCards))-1
        card = allAvailableCards[randomCardPosition].name
        return card

    def test_draft_first_random_character_card(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)

    def test_get_drafting_player(self):
        draftingPlayer = self.game.getDraftingPlayer()
        self.assertEqual('jeroen',draftingPlayer.name)

    def test_get_drafting_player_after_one_pick(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)
        draftingPlayer = self.game.getDraftingPlayer()
        self.assertEqual('robin',draftingPlayer.name)

    def test_draft_when_not_active_player(self):
        robinCard = self.getRandomCardName()
        with self.assertRaises(Exception):
             self.game.draftCharacterCard("robin",robinCard)

    def test_draft_when_not_active_player_after_pick(self):
        randomDraftPick = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen",randomDraftPick)
        randomDraftPick = self.getRandomCardName()
        with self.assertRaises(Exception):
             self.game.draftCharacterCard("jeroen",randomDraftPick)

    def test_player_is_character_after_draft_pick(self):
        randomDraftPick = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen",randomDraftPick)
        self.assertEqual(randomDraftPick,self.game.getPlayer("jeroen").character)
    
    def test_game_contains_all_character_cards(self):
        cardInGame = self.game.getAllCharacterCards()
        self.assertEqual(8, len(cardInGame))

    def test_draft_starts_with_correct_open_cards(self):
        cardsInGame = self.game.getAllCharacterCards()
        openCards = 0
        for card in cardsInGame:
            if card.open is True:
                self.assertNotEqual("koning",card.name)
                openCards = openCards + 1

        self.assertEqual(1, openCards)

    def test_available_cards_not_available_after_draft_pick(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen",jeroenCard)
        self.assertEqual(False, self.game.getCharacterCard(jeroenCard).available)

    def test_available_cards_not_available_after_three_draft_picks(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)
        robinCard = self.getRandomCardName()
        self.game.draftCharacterCard("robin", robinCard)
        sanderCard = self.getRandomCardName()
        self.game.draftCharacterCard("sander", sanderCard)

        koningCard = self.game.getCharacterCard(jeroenCard)
        magierCard = self.game.getCharacterCard(robinCard)
        bouwmeesterCard = self.game.getCharacterCard(sanderCard)

        self.assertEqual(False, koningCard.available)
        self.assertEqual(False, magierCard.available)
        self.assertEqual(False, bouwmeesterCard.available)

    def test_draft_unavailable_card(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)
        with self.assertRaises(Exception):
            self.game.draftCharacterCard("robin", jeroenCard)

    def test_available_cards_available_after_wrong_draft_pick(self):
        jeroenCard = self.getRandomCardName()
        self.game.draftCharacterCard("jeroen", jeroenCard)
        sanderCard = self.getRandomCardName()
        with self.assertRaises(Exception):
            self.game.draftCharacterCard("sander", sanderCard)
        
        unavailableCard = self.game.getCharacterCard(jeroenCard)
        availableCard = self.game.getCharacterCard(sanderCard)

        self.assertEqual(False, unavailableCard.available)
        self.assertEqual(True, availableCard.available)

#test if the game continues correctly when done drafter

    def test_everyone_is_the_correct_character_after_full_draft(self):
        draftedCards = self.runFullRandomDraft()
        self.assertEqual(draftedCards["jeroen"], self.game.getPlayer("jeroen").character)
        self.assertEqual(draftedCards["robin"], self.game.getPlayer("robin").character)
        self.assertEqual(draftedCards["sander"], self.game.getPlayer("sander").character)
        self.assertEqual(draftedCards["martijn"], self.game.getPlayer("martijn").character)
        self.assertEqual(draftedCards["casper"], self.game.getPlayer("casper").character)

    def test_game_goes_to_turns_after_draft(self):
        draftedCards = self.runFullRandomDraft()
        gamestate = self.game.getState()
        turnGameState = "RunCharacterTurnsGameState"
        self.assertEqual(turnGameState, gamestate)

if __name__ == '__main__':
    unittest.main()