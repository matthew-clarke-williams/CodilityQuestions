"""
# TapeEquilibrium

Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

A non-empty array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part
and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference
that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random


def solution(A):
    # Need to loop through each potential value for P
    min_diff = 100000 * 1000
    for P in range(len(A) - 1):
        sum_left = sum(A[:P+1])
        sum_right = sum(A[P+1:])
        abs_diff = abs(sum_right - sum_left)
        min_diff = min(min_diff, abs_diff)

    return min_diff



A = [3, 1, 2, 4, 3]

print(solution(A))


class TestExercise(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

    def test_simple(self):
        self.assertEqual(solution([1, 2]), 1)

    def test_double(self):
        self.assertEqual(solution([-1000, 1000]), 2000)

    def test_random(self):
        # Does not actually test anything but, for observation,
        # Does run it with randomized array lengths and values.
        N = random.randint(*(2, 100000))
        arr = [random.randint(*(-1000, 1000)) for _ in range(N)]
        print(solution(arr), N, "\n", arr)