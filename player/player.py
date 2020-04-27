# player.py

class Player(object):
    """
    A player defines a player and their current state
    """
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.gold = 3 

    def pick_character_card(self, character):
        self.character = character
    
    def getPlayerPosition(self):
            return self.position