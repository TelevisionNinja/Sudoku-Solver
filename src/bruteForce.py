from utils import generate_sudoku_string, generate_CSP
from backtracking import recursive_backtracking


def generate_assignment(CSP):
    # create a dictionary with the values as empty lists
    assignment = {var: [] for var in CSP.get("variables")}

    return assignment


def solve(grid_string):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)

    solution_found, final_assignments = recursive_backtracking(assignment, CSP)

    return generate_sudoku_string(solution_found, final_assignments, CSP)
