"""
MinPerimeterRectangle - Find the minimal perimeter of any rectangle whose area equals N.

An integer N is given, representing the area of some rectangle.
The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).
The goal is to find the minimal perimeter of any rectangle whose area equals N.
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

        (1, 30), with a perimeter of 62,
        (2, 15), with a perimeter of 34,
        (3, 10), with a perimeter of 26,
        (5, 6), with a perimeter of 22.

Write a function:
    def solution(N)
that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:
        N is an integer within the range [1..1,000,000,000].

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

#
https://app.codility.com/demo/results/trainingWAMZPR-DH7/
"""
import math
import unittest


def solution(N):
    """
    The closer to the square root of N, we get, the smaller the perimeter
    """
    sqrt_N = N ** 0.5
    if sqrt_N == math.ceil(sqrt_N):
        return int(4 * sqrt_N)
    else:
        sqrt_N = math.ceil(sqrt_N)

    min_perimeter = float('inf')

    # Check all factors up to the square root of N
    for i in range(1, sqrt_N + 1):
        if N % i == 0:
            other_factor = int(N / i)
            perimeter = 2*i + 2*other_factor
            if perimeter < min_perimeter:
                min_perimeter = perimeter

    return min_perimeter


# p = solution(30)
q = solution(1000000000)
print("Solution", q)

class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(1), 4)
        self.assertEqual(solution(2), 6)
        self.assertEqual(solution(3), 8)
        self.assertEqual(solution(4), 8)
        self.assertEqual(solution(5), 12)
        self.assertEqual(solution(30), 22)
        self.assertEqual(solution(1e9), 126500)
