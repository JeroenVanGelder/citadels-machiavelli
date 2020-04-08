from state_machines.player_turn_states import StartTurnState

class PlayerTurnDevice(object):
    def __init__(self):
        self.state = StartTurnState()

    def on_event(self, event):
        self.state = self.state.on_event(event)