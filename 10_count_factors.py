"""
CountFactors - Count factors of given number n.

A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:
    def solution(N)
that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24.
There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..2,147,483,647].
"""

import unittest

def solution(N):
    sqrt_N = N ** 0.5
    sqrt_N = int(sqrt_N)

    num_factors = 0
    for factor in range(1, sqrt_N + 1):
        if N % factor == 0:
            if factor * factor == N:
                num_factors += 1
            else:
                num_factors += 2

    return num_factors

x = solution(16)


def solution2(N):
    # Initialize a variable to count the factors
    factors_count = 0

    # Initialize a variable to iterate from 1 up to the square root of N
    i = 1

    # Loop through numbers from 1 up to the square root of N
    while i * i <= N:
        # If i is a factor of N, increment the factors count
        if N % i == 0:
            # If i is the square root of N, increment factors_count by 1
            if i * i == N:
                factors_count += 1
            # Otherwise, increment factors_count by 2 since both i and N/i are factors
            else:
                factors_count += 2
        # Move to the next number
        i += 1

    # Return the total count of factors
    return factors_count

x = solution(2147483646)
print(x)
print(solution2(2147483646))


class TestExercise(unittest.TestCase):
    def testvalues(self):
        self.assertEqual(solution(24), 8)
        self.assertEqual(solution(32), 6)
        self.assertEqual(solution(16), 5)

