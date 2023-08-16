#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    new_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
         # Create an empty row for the result matrix
         new_row = []

         # Iterate through each element in the row and compute the square
         for element in row:
              squared_value = element ** 2
              new_row.append(squared_value)

         # Append the squared row to the result matrix
         new_matrix.append(new_row)

         return new_matrix
