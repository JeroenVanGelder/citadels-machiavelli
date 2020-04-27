# state.py

class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        pass

    def on_event(self, event, *argv):
        """
        Handle events that are delegated to this State.
        """
        pass

    def get_allowed_actions(self):
        return self.allowedActions

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__