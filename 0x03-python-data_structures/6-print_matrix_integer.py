#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for subMatrix in matrix:
        if len(subMatrix) == 0:
            print()
        for i in range(len(subMatrix)):
            print(
                "{:d}".format(subMatrix[i]),
                end="\n" if i is len(subMatrix) - 1 else " ",
            )
