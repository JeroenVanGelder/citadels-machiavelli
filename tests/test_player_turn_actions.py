import unittest, random
from machiavalli_game import MachiavelliGame
from player.playerDescriptions import PlayerDescription
from tests.test_machiavelli_game import TestMachiavelliGame

class TestPlayerTurnActions(TestMachiavelliGame):

    def setUp(self):
        self.setStartedGameWith5Players()
        self.draftedCards = self.runFullRandomDraft()

    def test_players_can_take_their_turns(self):
        player = self.game.getCurrentPlayer().name
        action = "pick_gold"
        self.game.playerTakeAction(player, action)
        pass
    
    def test_players_can_pick_two_gold_at_the_start_of_their_turns(self):
        player = self.game.getCurrentPlayer()
        startingGold = player.getGold()
        action = "pick_gold"
        self.game.playerTakeAction(player.name, action)
        goldAfterAction = player.getGold()
        self.assertEqual(2, goldAfterAction - startingGold)

    def test_player_can_not_pick_two_gold_twice(self):
        player = self.game.getCurrentPlayer()
        action = "pick_gold"
        self.game.playerTakeAction(player.name, action)
        with self.assertRaises(Exception):
            self.game.playerTakeAction(player.name, action)

    def test_player_can_start_picking_building_cards_at_the_start_of_their_turns(self):
        player = self.game.getCurrentPlayer()
        startingCards = player.getBuildingCardsInHand()
        action = "pick_cards"
        self.game.playerTakeAction(player.name, action)
        selectedCards = self.game.getPlayerBuildingCardSelection(player.name)
        self.assertEqual(2, len(selectedCards))

    def test_player_can_pick_two_building_cards_at_the_start_of_their_turns(self):
        player = self.game.getCurrentPlayer()
        startingCards = player.getBuildingCardsInHand()
        action = "pick_cards"
        self.game.playerTakeAction(player.name, action)
        cardSelection = self.game.getPlayerBuildingCardSelection(player.name)
        selectedCard = cardSelection[1]
        self.game.playerSelectBuildingCard(player.name, selectedCard)
        self.assertIn(selectedCard, player.getBuildingCardsInHand())

    def test_player_can_not_pick_card_before_selecting(self):
        buildingCard = self.game.getAllAvailableBuildingCards()
        player = self.game.getCurrentPlayer()
        self.game.playerSelectBuildingCard(player.name, buildingCard[6])
        self.assertNotIn(buildingCard, player.getBuildingCardsInHand())

    def test_player_can_only_pick_cards_that_are_selected(self):
        player = self.game.getCurrentPlayer()
        action = "pick_cards"
        self.game.playerTakeAction(player.name, action)
        cardSelection = self.game.getPlayerBuildingCardSelection(player.name)
        selectedCard = cardSelection[1]
        randomBuildingCard = self.game.getAllAvailableBuildingCards()[1]
        self.game.playerSelectBuildingCard(player.name, randomBuildingCard)
        self.assertNotIn(randomBuildingCard, player.getBuildingCardsInHand())

    def test_player_cant_pick_building_cards_at_the_start_of_their_turns_twice(self):
        player = self.game.getCurrentPlayer()
        startingCards = player.getBuildingCardsInHand()
        action = "pick_cards"
        self.game.playerTakeAction(player.name, action)
        cardSelection = self.game.getPlayerBuildingCardSelection(player.name)
        selectedCard = cardSelection[1]
        falseSelectedCard = cardSelection[0]
        self.game.playerSelectBuildingCard(player.name, selectedCard)
        self.game.playerSelectBuildingCard(player.name, falseSelectedCard)
        self.assertIn(selectedCard, player.getBuildingCardsInHand())
        self.assertNotIn(falseSelectedCard, player.getBuildingCardsInHand())

    #bouwfase
    #speler kan een gebouw in hand bouwen
    def test_player_can_build_a_card(self):
        player = self.game.getCurrentPlayer()
        cardToBeBuild = player.getBuildingCardsInHand()[0].name
        action = "build_card"
        self.game.playerTakeAction(player.name, action, buildingCard=cardToBeBuild)
        allCardsPlayerBuild = player.getAllBuildingsInPlay()
        self.assertIn(cardToBeBuild,allCardsPlayerBuild)

if __name__ == '__main__':
    unittest.main()