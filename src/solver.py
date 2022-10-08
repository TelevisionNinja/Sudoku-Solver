from backtracking import solve as back_solve
from forwardChecking import solve as forward_solve
from arcConsistency import solve as arc_solve
from bruteForce import solve as brute_solve

'''
Each value is separated by a space
A zero means an empty cell on the sudoku grid
'''
grid_string = """
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
"""

# show single solution

print("single solutions\n")

# very slow
# print("brute force\n")
# brute_solve(grid_string)

print("backtracking\n")
back_solve(grid_string)

print("forward checking\n")
forward_solve(grid_string)

print("arc consistency\n")
arc_solve(grid_string)


# show multiple solutions

print("\nmultiple solutions\n")

# very slow
# brute_solve(grid_string, True)

print("-------------------------\nbacktracking\n")

back_solve(grid_string, True)

print("-------------------------\nforward checking\n")

forward_solve(grid_string, True)

print("-------------------------\narc consistency\n")

arc_solve(grid_string, True)
