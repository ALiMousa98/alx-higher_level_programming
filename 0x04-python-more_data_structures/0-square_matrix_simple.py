#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in range(len(matrix)):
        newRow = []
        for col in range(len(matrix[row])):
            newRow.append(matrix[row][col] * matrix[row][col])
        newMatrix.append(newRow)
    return newMatrix
