# import itertools
# import random

import abstraction.state

class State(abstraction.state.State):
    """
    Class representing a state of the sliding-block game as a board and the position of the empty cell
    For instance, [[1,2,3],[4,0,6],[7,5,8]], (1,1)
    """
    def __init__(self, board, empty_position=None):
        self.width = len(board[0])
        self.board = board
        if empty_position == None:
            self.empty_position = tuple()
            for x in range(self.width):
                for y in range(self.width):
                    if self.board[x][y] == 0:
                        self.empty_position = (x, y)
        else:
            self.empty_position = empty_position

    def copy(self):
        """
        Returns a clone of the current state
        """
        board = []
        for row in self.board:
            board.append([x for x in row])
        return State(board, self.empty_position)

    def move(self, movement):
        """
        Moves a tile by a certain move, whether legal or not
        """
        x, y = self.empty_position
        dx, dy = movement
        # Swap
        self.board[x][y], self.board[x+dx][y+dy] = self.board[x+dx][y+dy], self.board[x][y]
        self.empty_position = (x+dx, y+dy)
        return self

    def print_state(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row
    
    def __eq__(self, obj):
        return isinstance(obj, State) and obj.board == self.board

    def __hash__(self):
        return hash(str(self))
