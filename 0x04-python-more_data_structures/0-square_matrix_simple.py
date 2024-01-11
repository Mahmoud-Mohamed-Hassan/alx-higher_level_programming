#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda subMtx: list(map(lambda n: n**2, subMtx)), matrix))
