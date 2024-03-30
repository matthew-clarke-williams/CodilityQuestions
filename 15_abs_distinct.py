"""
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order.
The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:
  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6

The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this
array, namely 0, 1, 3, 5 and 6.

Write a function:

    def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:
  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
        array A is sorted in non-decreasing order.

Copyright 2009–2024 by Codility Limited. All Rights Reserved.

----
https://app.codility.com/demo/results/trainingSJNPZ2-5SB/

Think in terms of two sets of numbers: the negative numbers and the positive numbers.
For the set of positive numbers, we already have the subset, or tail, of the list.
For the negative numbers, we step through and gather all their absolute values into a set, stopping at zero.
Now merge the two sets.
And return the length of the resulting set.

Oops. This is probably not the prescribed "caterpillar" method, but it gets 100% nonetheless.
"""

def solution(A):
    abs_set = set()

    for element in A:
        abs_set.add(abs(element))

    abs_count = len(abs_set)

    return abs_count


import unittest
import numpy as np



class TestExercise(unittest.TestCase):
    """
    """
    def test_worst_case(self):
        N = 100000
        lb = -2147483648
        ub = 2147483647
        rand_array = np.random.randint(lb, ub, N)
        rand_array = [1, 23, 4, -2]

    def test_examples(self):
        self.assertEqual(solution([-5, -3, -1, 0, 3, 6]), 5)
