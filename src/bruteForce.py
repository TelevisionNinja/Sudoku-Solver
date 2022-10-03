from utils import none_inference, is_assignment_complete, get_unassigned_variable, generate_CSP_variables, generate_sudoku_string, grid_index_to_row_and_col, is_valid_assignment


def convert_assignment_to_grid_brute_force(assignment):
    """
    make a grid (2d array) from the assignment object
    """

    grid = [[0 for _ in range(9)] for _ in range(9)] 

    for key, dictValue in assignment.items():
        row, col = grid_index_to_row_and_col(key)

        if len(dictValue) != 0:
            grid[row][col] = dictValue[0]

    return grid


def is_consistent_brute_force(value, variable, assignment):
    grid = convert_assignment_to_grid_brute_force(assignment)

    for key, dictValue in assignment.items():
        if len(dictValue) != 0:
            if not is_valid_assignment(grid, value, variable):
                return False

    return True


def recursive_brute_force(assignment, CSP, inference_function = none_inference, is_consistent_function = is_consistent_brute_force):
    if is_assignment_complete(assignment):
        return True, assignment

    variable = get_unassigned_variable(assignment)

    for value in CSP.get("domains").get(variable):
        if is_consistent_function(value, variable, assignment):
            # add the value to the assignment
            assignment.get(variable).append(value)

            inference_state, new_CSP = inference_function(CSP, variable, assignment)
            if inference_state: # the inference is successful
                backtrack_state, new_assignment = recursive_brute_force(assignment, new_CSP, inference_function, is_consistent_function)
                if backtrack_state:
                    return True, new_assignment
                else:
                    assignment.get(variable).remove(value)
            else: # the inference fails (a domain became empty)
                assignment.get(variable).remove(value)

    return False, assignment


def solve(grid_string):
    CSP, assignment = generate_CSP_variables(grid_string)

    solution_found, final_assignments = recursive_brute_force(assignment, CSP)

    return generate_sudoku_string(solution_found, final_assignments, CSP)
