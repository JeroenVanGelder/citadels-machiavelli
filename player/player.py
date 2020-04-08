# player.py

class Player(object):
    """
    A player defines a player and their current state
    """
    
    def __init__(self, name, position):
        print ('A player joined the game: ', str(name))
        print ('Player placed in seat #', position)
        self.name = name
        self.position = position
        if(position == 1):
            self.character = 'King'

    def pick_character_card(self, character):
        self.character = character