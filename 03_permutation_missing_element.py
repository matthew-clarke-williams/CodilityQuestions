"""
# PermMissingElem
Find the missing element in a given permutation.

An array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)],
 which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

Copyright 2009–2022 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.
"""
import unittest
import random


def solution(A):
    sorted_A = sorted(A)

    missing_element = 1
    for element in sorted_A:
        if element != missing_element:
            return missing_element
        else:
            missing_element += 1

    return missing_element

def solution2(A):
    """
    Take the sum of the elements of A. Compare this to the expected sum of A and the
    difference will be the missing number
    """
    full_array = range(1, len(A) + 2)
    return sum(full_array) - sum(A)


A = [2, 3, 1, 5]
B = [5, 2, 1, 4, 9, 8, 3, 7]

print(solution(A), "SOL1: should be 4")
print(solution(B), "SOL1: should be 6")

print(solution2(A), "SOL2: should be 4")
print(solution2(B), "SOL2: should be 6")




class TestExercise(unittest.TestCase):

    INT_RANGE = (0, 100000)

    def test_example1(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)

    def test_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)

    def test_random(self):
        arr = [n for n in range(1, random.randint(*self.INT_RANGE))]
        missing = random.randint(0, len(arr))
        arr.remove(missing)
        self.assertEqual(solution(arr), missing)

    def test_maximum(self):
        arr = [n for n in range(1, self.INT_RANGE[1] + 1)]
        arr.pop()
        self.assertEqual(solution(arr), self.INT_RANGE[1])
        
        
class TestExercise(unittest.TestCase):

    INT_RANGE = (0, 100000)

    def test_example1(self):
        self.assertEqual(solution2([2, 3, 1, 5]), 4)

    def test_single(self):
        self.assertEqual(solution2([2]), 1)
        self.assertEqual(solution2([1]), 2)

    def test_random(self):
        arr = [n for n in range(1, random.randint(*self.INT_RANGE))]
        missing = random.randint(0, len(arr))
        arr.remove(missing)
        self.assertEqual(solution2(arr), missing)

    def test_maximum(self):
        arr = [n for n in range(1, self.INT_RANGE[1] + 1)]
        arr.pop()
        self.assertEqual(solution2(arr), self.INT_RANGE[1])
