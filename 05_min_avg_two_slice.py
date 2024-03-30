"""
MinAvgTwoSlice

Find the minimal average of any slice containing at least two elements.

https://codility.com/programmers/task/min_avg_two_slice/

A non-empty array A consisting of N integers is given.
A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A
(notice that the slice contains at least two elements).
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided
by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

contains the following example slices:

        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of a slice whose average is minimal.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting
position of the slice with the minimal average. If there is more than one slice
with a minimal average, you should return the smallest starting position of such
a slice.

For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
----------------

# Discussion

The brute force solution is to determine the average of every slice of the
sequence. That's a lot of sequences! Is there a better way?

The solution doesn't even need prefix-sums.  The 'trick' is not in the coding at
all, but in an appreciation in the nature of the problem.

For this problem, the lowest average of two, or three, points can not be bested by
a longer sequence of points.  We do not need to consider any longer sequences.

To illustrate, consider [1, -1, 1, -1].
The two-point averages all come to 0.
The four-point average also comes to 0; it cannot best the two-point averages.
The three-point averages are 0.33 and -0.33.
So the correct answer is index point 1.

If you extend that sequence with, say, 100, it changes nothing.
If you extend that sequence with -100, then the answer becomes [-1, -100] (-50.5)
which is the best pair.

So we need to pass over the sequence once, calculating the two, and three, point
averages and returning the best of those.  O(N)

https://app.codility.com/demo/results/training6P83U6-V79/
"""
import unittest
import random


RANGE_A = (2, 100000)
RANGE_N = (-10000, 10000)


def solution(A):
    """
    The minimal average slice must be of length 2 or 3 as any longer slices must be
    """
    min_avg = (A[0] + A[1]) / 2
    min_index = 0

    # First check all the length 2 slices
    for i in range(len(A) - 2):
        # Check if slice of length 2 has smaller average
        avg_2 = (A[i] + A[i + 1]) / 2
        if avg_2 < min_avg:
            min_avg = avg_2
            min_index = i

        # Check if slice of length 3 has smaller average
        avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3
        if avg_3 < min_avg:
            min_avg = avg_3
            min_index = i

    # Check last slice of length 2
    avg_last = (A[-2] + A[-1]) / 2
    if avg_last < min_avg:
        min_avg = avg_last
        min_index = len(A) - 2

    return min_index


class TestExercise(unittest.TestCase):
    """
    example: example test
    double_quadruple: two or four elements
    simple1: simple test, the best slice has length 3
    simple2: simple test, the best slice has length 3
    small_random: random, length = 100
    medium_range: increasing, decreasing (legth = ~100) and small functional
    medium_random: random, N = ~700
    large_ones: numbers from -1 to 1, N = ~100,000
    large_random: random, N = ~100,000
    extreme_values: all maximal values, N = ~100,000
    large_sequence: many seqeneces, N = ~100,000
    """

    def test_example(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]), 1)
        self.assertEqual(solution([5, 2, 2, 100, 1, 1, 100]), 4)
        self.assertEqual(solution([11, 2, 10, 1, 100, 2, 9, 2, 100]), 1)

    def test_three(self):
        self.assertEqual(solution([-3, -5, -8, -4, -10]), 2)
        self.assertEqual(solution([-8, -6, -10]), 0)
        self.assertEqual(solution([1, -1, 1, -1]), 1)

    def test_random(self):
        A = [random.randint(*RANGE_N) for _ in range(2, 10)]
        print(A)
        print(solution(A))

    def test_extreme(self):
        A = [RANGE_N[1]] * (RANGE_A[1] // 3) + [RANGE_N[0]] * (RANGE_A[1] // 3)
        idx = solution(A)
        print(idx, A[idx - 3 : idx + 3])
