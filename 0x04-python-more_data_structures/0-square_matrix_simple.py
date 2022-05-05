#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        square_value = map(lambda i: i ** 2, matrix[i])
        new_matrix.append(list(square_value))
    return new_matrix
