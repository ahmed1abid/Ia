class State:
    """
    Abstract class representing a state
    """

    def copy(self):
        """
        Return a new puzzle with the same plateau as 'self'
        """
        raise NotImplementedError

    def print_state(self):
        raise NotImplementedError

    def __str__(self):
        """
        Ttransform the current state into a string
        """
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
    
    def __eq__(self, obj):
        """
        Compares the current state to another
        """
        raise NotImplementedError

    def __hash__(self):
        return hash(str(self))
