#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return_matrix = matrix.copy()

    for i in range(len(matrix)):
        return_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (return_matrix)
