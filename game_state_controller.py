"""
This is the class that governs the state of the game. It functions as an application controller with build in state machine.
"""

from state_machines.game_states import StartingGameState

class GameStateController(object):

    def __init__(self):
        self.state = StartingGameState()

    def on_event(self, event):
        self.state = self.state.on_event(event)

    def get_game_state(self):
        return self.state

    def get_allowed_actions(self):
        return self.state.get_allowed_actions() 