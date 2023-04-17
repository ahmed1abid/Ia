import collections
import sys
from node import *


class Exploration:
    """
    Exploration algorithm
    - problem: Formalized problem to be solved
    - criterion: function that associates a node with a score, the lowest being the best
    - open: collection of nodes known but not yet explored
    - close: collection of nodes already explored
    - n_explores: number of nodes explored (useful for statistics at the end)
    """

    def __init__(self, problem, criterion):
        self.problem = problem
        self.criterion = criterion
        self.open = {}
        self.close = {}
        self.n_explores = 0

    def pick(self):
        """
        Return a new node to explore
        """
        # pick the node with the lowest f value from open
        min_node = None
        for node in self.open.values():
            if min_node is None or node.f < min_node.f:
                min_node = node
        return min_node
    


    def update_tree(self, new_nodes):
        """
        Updates the exploration tree with a new node
        """
        for new_node in new_nodes:
            if new_node.state in self.close:
                old_node = self.close[new_node.state]
                if new_node.g < old_node.g:
                    # replace the old node with the new node
                    del self.close[new_node.state]
                    self.open[new_node.state] = new_node
            elif new_node.state in self.open:
                old_node = self.open[new_node.state]
                if new_node.g < old_node.g:
                    # replace the old node with the new node
                    del self.open[new_node.state]
                    self.open[new_node.state] = new_node
            else:
                self.open[new_node.state] = new_node

    def explore(self):
        """
        Explores a state space and returns the found path,
        optionally None if no path is found
        """
        # initialize open with the initial state
        initial_node = Node(self.problem.initial_state, criterion=self.criterion)
        self.open[initial_node.state] = initial_node

        while self.open:
            # pick the node with the lowest f value from open
            current_node = self.pick()

            # move the current node from open to close
            del self.open[current_node.state]
            self.close[current_node.state] = current_node

            self.n_explores += 1

            if self.problem.goal(current_node.state):
                # goal found, backtrack to get the path
                return current_node.backtrack_path()

            # generate successor nodes
            new_nodes = []
            for action in self.problem.possible_actions(current_node.state):
                new_node = current_node.create_child(action, self.problem)
                new_nodes.append(new_node)

            # update the exploration tree with the new nodes
            self.update_tree(new_nodes)

        # no path found
        return None
