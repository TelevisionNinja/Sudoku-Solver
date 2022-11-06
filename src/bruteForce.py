from utils import generate_CSP
from backtracking import recursive_backtracking


def generate_assignment(CSP):
    # create a dictionary with the values as empty lists
    assignment = {var: [] for var in CSP.get("variables")}

    return assignment


def solve(grid_string, multipleSolutions = False):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)
    solutions = []

    recursive_backtracking(assignment, CSP, solutions, multipleSolutions)

    return solutions, CSP
