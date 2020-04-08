from state_machines.state import State

class StartTurnState(State):
    """
    The state a player has when starting his turn
    """
    def on_event(self, event):
        if event == 'start_turn':
            return ResourceState()
            
        return self

class ResourceState(State):
    """
    The state a player that started his turn have
    In this stage he picks his resource type
    """

    def on_event(self, event):
        if event == 'picked_resource':
            return EndTurnState()

        return self

class EndTurnState(State):
    """
    The player needs to end his turn
    """
    def on_event(self, event):
        if event == 'end_turn':
            return StartTurnState()

        return self