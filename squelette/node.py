
class Node:
    """
   Class representing a node that contains
    - 'state', a state
    - 'parent', the node's predecessor, optionally None if none
    - 'action', the action that led to this node
    - 'g', the cumulative cost, 0 if none
    - 'criterion', the function that calculates f from a node
    - 'f', the score used to pick in OPEN, g if none
    """
    def __init__(self, state, g=None, criterion=None, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.criterion=criterion
        if (g == None):
            self.g = 0
        else:
            self.g = g
        if (criterion == None):
            self.criterion = lambda node: node.g
        else:
            self.criterion = criterion

    def backtrack_path(self):
        """
        Rebuild the path from the root of the exploration tree
        """
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        return list(reversed(p))

    def create_child(self, action, problem):
        """
        Creates a new node from the current one by applying a given action.
        The action is assumed to be valid.
        """
        new_state = problem.transition(self.state, action)
        new_g = self.g + problem.cost(self.state, action)
        return Node(new_state,\
                     parent=self,\
                     action=action,\
                     g=new_g,
                     criterion=self.criterion)

    @property
    def f(self):
        return self.criterion(self)

    def __str__(self):
        return str(self.state)+" / "+str(self.f)

