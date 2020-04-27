from state_machines.state import State

class StartingGameState(State):
    """
    The state of the game when it starts
    """
    def __init__(self):
        State.__init__(self)
        self.allowedActions=list()
        self.allowedActions.extend(["registerPlayer","startGame"])

    def on_event(self, event, *argv):
        if event == 'startGame':
            return DraftCharacterCardsGameState()
        return self
    
    def __repr__(self):
        return "starting"

class DraftCharacterCardsGameState(State):
    """
    placeholder
    """
    def __init__(self):
        State.__init__(self)
        self.allowedActions=list()
        self.allowedActions.extend(["draftCharacterCards"])

    def on_event(self, event, *argv):
        if event == 'start_game':
            return StartGameState()

        return self
