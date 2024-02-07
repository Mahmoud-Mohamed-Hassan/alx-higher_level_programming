#!/usr/bin/python3
"""pascal_triangle Function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    triangles_list = [[1]]
    while len(trianngles_list) != n:
        last_row = triangles_list[-1]
        temp = [1]
        for i in range(len(last_row) - 1):
            temp.append(last_row[i] + last_row[i + 1])
        temp.append(1)
        triangles_list.append(temp)
    return triangles_list
