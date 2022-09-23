#!/usr/bin/python3
"""Matrix"""


def matrix_divided(matrix, div):
    """Write a function that divides all elements of a matrix"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    m = []
    for j in range(len(matrix)):
        if length is not len(matrix[j]):
            raise TypeError("Each row of the matrix must have the same size")
        m.append([])
        for i in matrix[j]:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            m[j].append(round(i / div, 2))
    return m
