import random
import abstraction.problem
from taquin.action import Action
from taquin.state import State

class Problem(abstraction.problem.Problem):
    """
    Class representing the teaser problem as:
    - an initial state
    - a goal() predicate
    - a transition() method
    """
    def __init__(self, initial_state, final_state):
        self.initial_state = initial_state
        self.final_state = final_state

    def get_initial_state(self):
        """
        Returns the initial state
        """
        return self.initial_state

    def goal(self, state):
        """
        Returns true if the state in parameter is a goal state
        """
        return state == self.final_state

    @classmethod
    def possible_actions(cls, state):
        """
        Returns the list of possible actions from a given state
        """
        actions = []
        x, y = state.empty_position
        for action in Action.possible_actions():
            dx, dy = action.vector()
            if x+dx >= 0 and y+dy >= 0 and x+dx < state.width and y+dy < state.width:
                actions.append(action)
        return actions

    @classmethod
    def transition(cls, current_state, action):
        """
        Returns the new state reached from a current state by a given action
        """
        return current_state.copy().move(action.vector())

    @classmethod
    def cost(cls, current_state, action):
        """
        Returns the cost of an action from a given state
        """
        return 1

    def heuristic_manhattan(self, state):
        """
        A heuristic function that calculates the sum of L1 distances
        between current and target position for each tile
        This heuristic is admissible.
        """
        x_values = [0]*((state.width*state.width)-1)
        y_values = [0]*((state.width*state.width)-1)
        for x in range(state.width):
            for y in range(state.width):
                # Memorize current and target positions
                # If not the empty cell
                if state.board[x][y] != 0:
                    x_values[state.board[x][y]-1] += x
                    y_values[state.board[x][y]-1] += y
                if self.final_state.board[x][y] != 0:
                    x_values[self.final_state.board[x][y]-1] += -x
                    y_values[self.final_state.board[x][y]-1] += -y
        return sum(map(abs, x_values))+sum(map(abs, y_values))

    def heuristic_misplaced(self, state):
        """
        A heuristic function that calculates the number of misplaced tiles
        between current and target positions
        This heuristic is admissible.
        """
        misplaced_tiles = 0
        for x in range(state.width):
            for y in range(state.width):
                if state.board[x][y] != self.final_state.board[x][y]:
                    misplaced_tiles += 1
        return misplaced_tiles
