from utils import generate_CSP_variables, generate_sudoku_string
from backtracking import recursive_backtracking
import copy


def conflicts(x, y):
    return x == y


def revise_sudoku(CSP, Xi, Xj):
    revised = False
    new_CSP = copy.deepcopy(CSP)

    for x in CSP.get("domains").get(Xi):
        broken = False

        for y in CSP.get("domains").get(Xj):
            if not conflicts(x, y):
                broken = True
                break

        if not broken:
            new_CSP.get("domains").get(Xi).remove(x)
            revised = True

    return revised, new_CSP


def arc_consistency(CSP, revise):
    queue = [(Xi, Xj) for Xi in CSP.get("variables") for Xj in CSP.get("neighbors").get(Xi)] 

    while len(queue) != 0:
        Xi, Xj = queue.pop(0)

        revise_state, new_CSP = revise(CSP, Xi, Xj)
        if revise_state: # the domain of Xi has been changed
            if len(new_CSP.get("domains").get(Xi)) == 0:
                return False, new_CSP

            for xk in new_CSP.get("neighbors").get(Xi):
                if xk != Xj:
                    queue.append((xk, Xi))

            CSP = new_CSP

    return True, CSP


def solve(grid_string):
    CSP, assignment = generate_CSP_variables(grid_string)

    is_arc_consistent, new_csp = arc_consistency(CSP, revise_sudoku)
    solution_found, final_assignments = recursive_backtracking(assignment, new_csp)

    return generate_sudoku_string(solution_found, final_assignments, new_csp)
