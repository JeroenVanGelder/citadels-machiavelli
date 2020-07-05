class PlayerActionsController(object):

    def __init__(self):
        print("success")

    def getPlayerAction(self, action):
        return {
            'pick_gold': self.pickGold,
            'pass_turn': self.passTurn,
            'pick_cards': self.pickCards,
            'select_picked_card': self.selectPickedCard,
        }.get(action)

    def pickCards(self, player):
        pass
    
    def selectPickedCard(self, player, card):
        pass

    def passTurn(self,player):
        self.activePlayingPlayerPosition += 1

    def pickGold(self, player):
        if player.pickedStartingResource is False:
            self.addPlayerGold(player, 2)
            player.pickedStartingResource = True
        else:
            raise Exception("Player already picked a resource")
