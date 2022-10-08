from utils import none_inference, is_consistent, is_assignment_complete, get_unassigned_variable, generate_CSP, generate_sudoku_string, generate_assignment
import copy

def recursive_backtracking(assignment, CSP, solutions, multipleSolutions = False, inference_function = none_inference, is_consistent_function = is_consistent):
    if is_assignment_complete(assignment):
        if multipleSolutions:
            solutions.append(copy.deepcopy(assignment))
            return False

        solutions.append(assignment)
        return True

    variable = get_unassigned_variable(assignment)

    for value in CSP.get("domains").get(variable):
        if is_consistent_function(value, variable, assignment, CSP):
            # add the value to the assignment
            assignment.get(variable).append(value)

            inference_state, new_CSP = inference_function(CSP, variable, assignment)

            if inference_state: # the inference is successful
                backtrack_state = recursive_backtracking(assignment, new_CSP, solutions, multipleSolutions, inference_function, is_consistent_function)

                if backtrack_state and not multipleSolutions:
                    return True

            # the inference fails (a domain became empty)
            assignment.get(variable).remove(value)

    return False


def solve(grid_string, multipleSolutions = False):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)
    solutions = []

    recursive_backtracking(assignment, CSP, solutions, multipleSolutions)

    if len(solutions) == 0:
        print("No solution found")
    else:
        for solution in solutions:
            print(generate_sudoku_string(solution, CSP))
            print()
