import abstraction.action

class Action(abstraction.action.Action):
    """
    Class representing an action in the teaser game
    """

    # Static possible actions
    directions = {'Right':( 0,-1),
                  'Left':( 0, 1),
                  'Down':   ( 1, 0),
                  'Up':  (-1, 0)}
        
    @classmethod
    def possible_actions(cls):
        """
        Returns the list of all possible actions
        """
        return map(lambda k: Action(k), Action.directions.keys())

    def __init__(self, direction):
        self.direction = direction

    def vector(self):
        """
        Returns the displacement vector associated with the action
        """
        return Action.directions[self.direction]
    
    def __str__(self):
        return self.direction

