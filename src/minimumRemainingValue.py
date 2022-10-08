from utils import generate_CSP, generate_sudoku_string, generate_assignment, is_consistent, get_unassigned_variable as get_first_unassigned_variable
from backtracking import recursive_backtracking
from forwardChecking import forward_checking


def get_unassigned_variable(assignment, CSP):
    minimumDomainSize = 10 # set it to the max domain size
    selectedVariable = None

    for variable, assigned_value in assignment.items():
        if len(assigned_value) == 0: # check if the variable has been assigned
            domainSize = len(CSP.get("domains").get(variable))

            if domainSize < minimumDomainSize:
                minimumDomainSize = domainSize
                selectedVariable = variable

    if selectedVariable is None:
        selectedVariable = get_first_unassigned_variable(assignment, CSP)

    return selectedVariable


def solve(grid_string, multipleSolutions = False):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)
    solutions = []

    recursive_backtracking(assignment, CSP, solutions, multipleSolutions, forward_checking, is_consistent, get_unassigned_variable)

    for solution in solutions:
        print(generate_sudoku_string(solution, CSP))
        print()
