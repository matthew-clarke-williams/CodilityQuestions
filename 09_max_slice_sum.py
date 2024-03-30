"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a
slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
"""


def solution(A):
    """
    Given an array A consisting of N integers, returns the maximum sum of any slice of A.

    Should have time complexity O(N)
    """
    max_slice_sum = A[0]  # Initialize with the first element
    max_ending_cur_slice = A[0]  # Initialize with the first element

    for num in A[1:]:  # Iterate through the array starting from the second element
        max_ending_cur_slice = max(num, max_ending_cur_slice + num)
        max_slice_sum = max(max_slice_sum, max_ending_cur_slice)
    return max_slice_sum

# Test the function
A = [3, 2, -6, 4, 0]
print(solution(A))  # Output should be 5