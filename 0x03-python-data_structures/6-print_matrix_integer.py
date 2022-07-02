#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for layer in matrix:
        for i in range(len(layer)):
            if i != len(layer) - 1:
                print("{:d}".format(layer[i]), end=" ")
            else:
                print("{:d}".format(layer[i]))
