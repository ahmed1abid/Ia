
import random

class Problem:
    """
    Abstract class that summarizes the methods needed for a problem
    """
    
    def get_initial_state(self):
        """
       Returns the initial state
        """
        raise NotImplementedError
    
    def goal(self, state):
        """
        Returns true if the state in parameter is a goal state
        """
        raise NotImplementedError

    @classmethod
    def possible_actions(cls, state):
        """
        Returns the list of possible actions from a given state
        """
        raise NotImplementedError

    @classmethod
    def transition(cls, current_state, action):
        """
        Returns the new state reached from a current state by a given action
         CAUTION: the input state must not be modified. You have to make a copy.
        """
        raise NotImplementedError

    @classmethod
    def successors(cls, state):
        """
        Returns the possible successor states of a given state
        """
        for action in cls.possible_actions(state):
            yield cls.transition(state, action)

    @classmethod
    def cost(current_state, action):
        """
        Returns the cost of an action from a given state
        """
        raise NotImplementedError

    @classmethod
    def mix_up(cls, state, n=100):
        """
        Returns a mixed-up state
        """
        # Make n consecutive random moves
        for _ in range(n):
            actions = cls.possible_actions(state)
            r = random.randint(0, len(actions)-1)
            state = cls.transition(state, actions[r])
        return state


