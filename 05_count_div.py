"""
# CountDiv

Compute number of integers divisible by k in range [a..b].

Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are
divisible by K, i.e.:

    { i : A <= i <= B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three
numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

    * A and B are integers within the range [0..2,000,000,000];
    * K is an integer within the range [1..2,000,000,000];
    * A ≤ B.

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest


def my_solution(A, B, K):
    num_int_divis = 0
    for value in range(A, B+1):
        if value % K == 0:
            num_int_divis += 1

    return num_int_divis

print(my_solution(6, 11, 2))

def solution(A, B, K):
    # Number of integers divisible by K up to B
    count_B = B // K

    # Number of integers divisible by K up to A-1
    count_A = (A - 1) // K if A > 0 else 0

    # Return the count of integers divisible by K within the range [A..B]
    return count_B - count_A

N = solution(0, 0, 1)
print("N = ", N)


class TestExercise(unittest.TestCase):
    """
    example
    simple (11, 345, 17)
    minimal: A = B in {0,1}, K=11
    extreme_ifempty: A=10, B=10, K in {5,7,20}
    extreme_endpoints: verify handling of range endpoints, multiple runs
    big_values: (100, 123e6, K=10e3)
    big_values2: (101, 123M+, 10K)
    big_values3: (0, maxint, k in {1, maxint}
    big_values4: A, B, K in {1,maxint}
    """

    def test_example(self):
        self.assertEqual(3, solution(6, 11, 2))

    def test_small(self):
        self.assertEqual(3, solution(5, 11, 2))
        self.assertEqual(4, solution(6, 12, 2))
        self.assertEqual(4, solution(5, 12, 2))
        self.assertEqual(4, solution(5, 13, 2))

    def test_edges(self):
        self.assertEqual(solution(0, 0, 1), 1)
        self.assertEqual(solution(0, 1, 1), 2)
        self.assertEqual(solution(1, 1, 2), 0)

    def test_more_edges(self):
        self.assertEqual(solution(9, 21, 10), 2)
        self.assertEqual(solution(10, 20, 10), 2)
        self.assertEqual(solution(10, 21, 10), 2)
        self.assertEqual(solution(11, 21, 10), 1)
        self.assertEqual(solution(11, 20, 10), 1)

    def test_max_min(self):
        max_int = int(2e9)
        self.assertEqual(solution(0, max_int, 1), max_int + 1)




fin = 1