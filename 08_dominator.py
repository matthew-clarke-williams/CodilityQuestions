"""
An array A consisting of N integers is given.
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7)
and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A
occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
import unittest


def solution(A):
    """
    For an element to be dominant in A, it needs to occur more than half the length of A
    """
    # First check edge cases
    if len(A) == 0:
        return -1

    # First count frequency of each element
    freq_dict = {}
    for element in A:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    # Find most frequent
    max_count = 0
    max_count_element = None
    for element in freq_dict:
        if freq_dict[element] > max_count:
            max_count = freq_dict[element]
            max_count_element = element

    # Check if dominant
    min_req_for_dominant = int(len(A) / 2) + 1
    if max_count >= min_req_for_dominant:
        # max count element is a dominant
        dominant_index = A.index(max_count_element)
        return dominant_index

    else:
        return -1



A = [3, 4, 3, 2, -1, 3, 3]
x = solution(A)
print(x)

class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        self.assertEqual(solution(A), 0)

    def test_empty(self):
        self.assertEqual(solution([]), -1)

    def test_half(self):
        B = [3, 4, 3, 2, -1, 3, 3]
        self.assertEqual(solution(B), 0)

    def test_half(self):
        C = [3, 4, 3, 2, -1, 3, 3, 6]
        self.assertEqual(solution(C), -1)

