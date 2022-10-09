#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = list((map(lambda _: _ * _, new_matrix[i])))
    return new_matrix
