from utils import none_inference, is_consistent, is_assignment_complete, get_unassigned_variable, generate_CSP, generate_sudoku_string, generate_assignment


def recursive_backtracking(assignment, CSP, inference_function = none_inference, is_consistent_function = is_consistent):
    if is_assignment_complete(assignment):
        return True, assignment

    variable = get_unassigned_variable(assignment)

    for value in CSP.get("domains").get(variable):
        if is_consistent_function(value, variable, assignment, CSP):
            # add the value to the assignment
            assignment.get(variable).append(value)

            inference_state, new_CSP = inference_function(CSP, variable, assignment)
            if inference_state: # the inference is successful
                backtrack_state, new_assignment = recursive_backtracking(assignment, new_CSP, inference_function, is_consistent_function)
                if backtrack_state:
                    return True, new_assignment
                else:
                    assignment.get(variable).remove(value)
            else: # the inference fails (a domain became empty)
                assignment.get(variable).remove(value)

    return False, assignment


def solve(grid_string):
    CSP = generate_CSP(grid_string)
    assignment = generate_assignment(CSP)

    solution_found, final_assignments = recursive_backtracking(assignment, CSP)

    return generate_sudoku_string(solution_found, final_assignments, CSP)
