import numpy as np

def gauss_jordan_eliminator(matrix):
    """
        @Link for pseudocode of Gauss-Jordan elimination on a binary matrix that was use as skeleton
        https://www.cs.umd.edu/~gasarch/TOPICS/factoring/fastgauss.pdf
    """
    size = matrix.shape[0]

    for j in range(size):
        pivot_row = None


        for i in range(j, size):
            if matrix[i][j] == 1:
                pivot_row = i
                break

        if pivot_row is not None:

            if pivot_row != j:
                matrix[[j, pivot_row]] = matrix[[pivot_row, j]]

            for i in range(j + 1, size):
                if matrix[i][j] == 1:
                    matrix[i] = np.bitwise_xor(matrix[i], matrix[j])

    for i in range(size - 1, -1, -1):

        for j in range(i - 1, -1, -1):
            if matrix[j][i] == 1:
                matrix[j] = np.bitwise_xor(matrix[j], matrix[i])

    return matrix

def toggle_matrix_creation(row_size, column_size):

    size = row_size * column_size
    toggle_matrix = np.zeros((size, size), dtype=int)

    for index in range(size):
        res = divmod(index, column_size)

        row = res[0]
        col = res[1]

        toggle_matrix[index][index] = 1

        if row > 0:
            toggle_matrix[index][index - column_size] = 1

        if row < row_size - 1:
            toggle_matrix[index][index + column_size] = 1

        if col > 0:
            toggle_matrix[index][index - 1] = 1

        if col < column_size - 1:
            toggle_matrix[index][index + 1] = 1

    return toggle_matrix

def get_heuristic_solution(field,row_size, column_size):
    prepared_field = np.array(field, dtype=int)

    toggle_matrix = toggle_matrix_creation(row_size, column_size)

    matrix = np.column_stack(
        (toggle_matrix,
         np.array(prepared_field, dtype=int))
    )

    solution_matrix = gauss_jordan_eliminator(matrix)

    return solution_matrix[:, -1]

