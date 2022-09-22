#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Write a function that divides all elements of a matrix"""
    

    def matrix_divided(matrix, div):
        """Matrix"""
        new_matrix = list(matrix)
        if not isinstance(matrix, [[]]) or not isinstance(matrix, float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for row in matrix:
            if matrix is not len(matrix):
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div, int) or not isinstance(div, float):
                raise TypeError("div must be a number")
            if div is not 0:
                raise ZeroDivisionError("division by zero")
            matrix[[]] % div
            return new_matrix
