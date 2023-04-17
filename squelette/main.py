import time
from node import Node
from exploration import Exploration
from taquin.problem import Problem
from taquin.state import State


###############################################
# Taquin
###############################################

board = [[1,2,3],[4,5,0],[6,7,8]]
goal = [[1,2,3],[4,5,6],[7,8,0]]

target_state = State(goal)

initial_state = State(board)
# OU
# initial_state = State(board) = Probleme.mix_up(target_state)

problem = Problem(initial_state=initial_state, final_state=target_state)

# Dijkstra
# score_function = lambda node: node.g


#heuristic_manhattan:
score_function = lambda node: problem.heuristic_manhattan(node.state)

# A*
# score_function = lambda node: node.g + problem.heuristic_manhattan(node.state)

# A* misp
score_function = lambda node: node.g + problem.heuristic_misplaced(node.state)


###############################################
# Exploration (generic)
###############################################

exploration = Exploration(problem=problem, criterion=score_function)
time_begin = time.process_time()
path = exploration.explore()
time_end = time.process_time()

###############################################
# Result
###############################################
print("=====================================================")
steps = -1
print("Initial state:\t" + str(problem.initial_state))
if path is not None and len(path) > 0:
    last = None
    for node in path:
        print(node.action)
        node.state.print_state()
        time.sleep(0.2)
        last = node
        steps += 1
        print(last)
    print("Final state:\t\t" + str(last.state))
    print("Total cost:\t\t" + str(last.g))
else:
    print("Goal not achievable")

print("Number of nodes explored:" + str(exploration.n_explores))
print("Number of steps: " + str(steps))
print("Exploration duration: " + str(time_end - time_begin) + " second(s)") 
