import numpy as np
import pandas as pd

def solution(A):
    # Filter out non-positive values and get unique positive values
    A_positive_unique = sorted(set(x for x in A if x > 0))

    # Find the smallest positive integer not present
    smallest_positive = 1
    for value in A_positive_unique:
        if value == smallest_positive:
            smallest_positive += 1
        else:
            break

    return smallest_positive


A = [-10, 1, 17, 3, 6, -4, 6, 2, 4, 1, 2]

lowest_num = solution(A)




fin=1