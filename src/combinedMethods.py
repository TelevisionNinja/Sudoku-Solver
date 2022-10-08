from utils import is_consistent, generate_CSP, generate_sudoku_string, generate_assignment
from backtracking import recursive_backtracking
from forwardChecking import forward_checking
from arcConsistency import arc_consistency
from minimumRemainingValue import get_unassigned_variable
from leastConstrainingValue import get_domain


def solve(grid_string, multipleSolutions = False):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)
    solutions = []

    is_arc_consistent, new_csp = arc_consistency(CSP)
    recursive_backtracking(assignment, new_csp, solutions, multipleSolutions, forward_checking, is_consistent, get_unassigned_variable, get_domain)

    if len(solutions) == 0:
        print("No solution found")
    else:
        for solution in solutions:
            print(generate_sudoku_string(solution, CSP))
            print()
