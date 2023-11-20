import numpy as np

def gauss_jordan_binary(matrix):
    """
    Performs Gauss-Jordan elimination on a binary matrix (0s and 1s).
    The function assumes the matrix is valid (contains only 0s and 1s) and is square.
    """
    n = len(matrix)

    for i in range(n):
        # Make the diagonal element 1 if it's not already.
        if matrix[i][i] == 0:
            for j in range(i+1, n):
                if matrix[j][i] == 1:
                    # Swap rows
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break

        # Make all elements below the diagonal in current column 0
        for j in range(i+1, n):
            if matrix[j][i] == 1:
                # Perform row operation
                matrix[j] = (matrix[j] + matrix[i]) % 2

    # Back substitution to make the upper triangle 0
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if matrix[j][i] == 1:
                matrix[j] = (matrix[j] + matrix[i]) % 2

    return matrix

A = np.array([
    [1,1,0,1,0,0,0,0,0],
    [1,1,1,0,1,0,0,0,0],
    [0,1,1,0,0,1,0,0,0],
    [1,0,0,1,1,0,1,0,0],
    [0,1,0,1,1,1,0,1,0],
    [0,0,1,0,1,1,0,0,1],
    [0,0,0,1,0,0,1,1,0],
    [0,0,0,0,1,0,1,1,1],
    [0,0,0,0,0,1,0,1,1]
], dtype=int)

b = np.array([1,1,0,1,0,0,0,1,0], dtype=int)

# Augmenting the matrix A with b
augmented_matrix = np.column_stack((A, b))

# Performing Gauss-Jordan elimination on the augmented matrix
result_augmented_matrix = gauss_jordan_binary(augmented_matrix)


print(result_augmented_matrix)
