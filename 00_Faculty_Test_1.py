"""
Solve this problem in Python. Use comments in the code to clearly describe the steps and why each step is taken.


"""
import unittest

def solution(A):
    """
    Given array A of N integers between (-100, 100) returns the sign of the product of all
    numbers in the array multiplied together
    """
    count_neg = 0
    for number in A:
        if number == 0:
            return 0
        elif number < 0:
            count_neg += 1

    if count_neg != 0 and count_neg % 2 != 0:
        # There is an odd number of negative numbers in A and so the product is negative
        return -1
    else:
        return 1





class TestExercise(unittest.TestCase):
    """
    """
    def test_positive(self):
        self.assertEqual(solution([1, -2, -3, 5]), 1)

    def test_negative(self):
        self.assertEqual(solution([1, 2, 3, -5]), -1)

    def test_zero(self):
        self.assertEqual(solution([1, 2, 0, -5]), 0)
