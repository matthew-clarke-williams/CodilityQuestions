"""
# Passing Cars

Count the number of passing cars on the road.

A non-empty array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q),
where 0 ≤ P < Q < N, is passing when P is traveling to the east
and Q is traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random


MAX_PAIRS = int(1e9)

def solution(A):
    # First set the number of passing cars to be 0
    passing_cars = 0
    count_east = 0

    # Iterate through the array
    for car in A:
        if car == 0:
            # Car is travelling east
            count_east += 1
        else:
            # Car is travelling west
            passing_cars += count_east    # Each west car will pass all of the known east cars
            # Check if the number of passing cars exceeds the limit
            if passing_cars > MAX_PAIRS:
                return -1

    return passing_cars


# Test the function
A = [0, 1, 0, 1, 1]
print(solution(A))  # Output should be 5

fin = 1



class TestExercise(unittest.TestCase):
    """
    example: example test
    single: single element
    double: two elements
    simple: simple test
    small_random: random, length = 100
    small_random2: random, length = 1000
    medium_random: random, length = ~10,000
    large_random: random, length = ~100,000
    large_big_answer: 0..01..1, length = ~100,000
    large_alternate: 0101..01, length = ~100,000
    large_extreme: large test with all 1s/0s, length = ~100,000
    """

    def test_example(self):
        self.assertEqual(solution([0, 1, 0, 1, 1]), 5)

    def test_minimal(self):
        self.assertEqual(solution([0]), 0)
        self.assertEqual(solution([1]), 0)
        self.assertEqual(solution([0, 0]), 0)
        self.assertEqual(solution([1, 1]), 0)
        self.assertEqual(solution([0, 1]), 1)
        self.assertEqual(solution([1, 0]), 0)

    def test_three(self):
        self.assertEqual(solution([0, 0, 0]), 0)
        self.assertEqual(solution([0, 0, 1]), 2)
        self.assertEqual(solution([0, 1, 0]), 1)
        self.assertEqual(solution([0, 1, 1]), 2)
        self.assertEqual(solution([1, 0, 0]), 0)
        self.assertEqual(solution([1, 0, 1]), 1)
        self.assertEqual(solution([1, 1, 0]), 0)
        self.assertEqual(solution([1, 1, 1]), 0)

    def test_four(self):
        self.assertEqual(solution([0, 0, 0, 0]), 0)
        self.assertEqual(solution([0, 0, 0, 1]), 3)
        self.assertEqual(solution([0, 0, 1, 1]), 4)
        self.assertEqual(solution([0, 1, 0, 0]), 1)
        self.assertEqual(solution([0, 1, 0, 1]), 3)
        self.assertEqual(solution([0, 1, 1, 1]), 3)
        self.assertEqual(solution([1, 0, 0, 0]), 0)
        self.assertEqual(solution([1, 0, 0, 1]), 2)
        self.assertEqual(solution([1, 0, 1, 0]), 1)
        self.assertEqual(solution([1, 0, 1, 1]), 2)
        self.assertEqual(solution([1, 1, 0, 0]), 0)
        self.assertEqual(solution([1, 1, 0, 1]), 1)
        self.assertEqual(solution([1, 1, 1, 0]), 0)
        self.assertEqual(solution([1, 1, 1, 1]), 0)

    def test_extreme(self):
        self.assertEqual(-1, solution([random.randint(0, 1) for _ in range(int(1e6))]))

