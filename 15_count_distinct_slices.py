"""
CountDistinctSlices
Count the number of distinct slices (containing only unique numbers).

https://app.codility.com/programmers/lessons/15-caterpillar_method/count_distinct_slices/


An integer M and a non-empty array A consisting of N non-negative integers are given.
All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
The slice consists of the elements A[P], A[P + 1], ..., A[Q].
A distinct slice is a slice consisting of only unique numbers.
That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2

There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

    def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2

the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..M].

Copyright 2009–2024 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.

--------------------------
! a distinct slice cannot be longer than M, as more would need duplicate values.
! watch that Q does not run off the end of the list
! watch that the count does not run over 1,000,000,000

The 70% solution comes relatively 'easy' but the 100% solution was too hard for me.

For 70% invokes two loops over the sequence which mark a 'sliding window' over
the array.  We loop over the values in the window to count the the unique sequences.
https://app.codility.com/demo/results/trainingUSRTK6-NWX/

The 100% solution requires two intertwined 'aha!' moments:
1. introduce a data structure which tracks the values currently inside the window
2. replace the innermost loop, to count sequences inside the window, with a
formula

The data structure, which I've called 'sequence', is a list of booleans which
mark whether or not that value is already inside the window.  With this we
can decide whether it is time to extend the right side of the window, because
the next number is not already inside the window, or not. The 'caterpiller' will gooble
up numbers to the right so long as they are not duplicates, then will bring up
tail until the duplicate drops out of the window.

When approached this way, just by maths, the number of sequences to add to the
count is a factor of the length of the sequence.  So, rather than looping
to identify each and every one, we can simply add the length of the sequence to
the count.

https://app.codility.com/demo/results/trainingJURN9A-8VM/

The debug for their example looks like:

end that moved, value added/dropped, left index, right index, window values, count, sequence
right 3 0 0 [] 0 [False, False, False, False, False, False, False]
right 4 0 1 [3] 1 [False, False, False, True, False, False, False]
right 5 0 2 [3, 4] 3 [False, False, False, True, True, False, False]
left 3 0 3 [3, 4, 5] 6 [False, False, False, True, True, True, False]
left 4 1 3 [4, 5] 6 [False, False, False, False, True, True, False]
left 5 2 3 [5] 6 [False, False, False, False, False, True, False]
right 5 3 3 [] 6 [False, False, False, False, False, False, False]
right 2 3 4 [5] 7 [False, False, False, False, False, True, False]
left 5 3 5 [5, 2] 9 [False, False, True, False, False, True, False]
left 2 4 5 [2] 9 [False, False, True, False, False, False, False]
"""
import unittest


def solution(M, A):
    count_dist_slice = 0
    N = len(A)

    # First, we do not need to check combinations that are of the form (k, k) since they will always be slices and
    # there are N of these
    for i in range(N):
        distinct = set()  # Initialize a set to store unique elements in the current slice
        for j in range(i, N):
            if A[j] not in distinct:
                distinct.add(A[j])
                count_dist_slice += 1  # Increment count for each distinct slice
                if count_dist_slice >= 1000000000:  # If count exceeds the limit, return the limit
                    return 1000000000
            else:
                break

    return count_dist_slice

    # a = A
    # m = M
    # result = 0
    # for left in range(len(a)):
    #     for right in range(left + 1, len(a)):
    #         # print(left, right, a[right], a[left:right])
    #         if a[right] in a[left:right]:
    #             break
    #         result += 1
    #         if result >= 1000000000:
    #             return 1000000000
    # return result + len(a)


# Example usage:
M = 6
A = [3, 4, 5, 5, 2]
print(solution(M, A))  # Output should be 9



class TestExercise(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution(0, [0]), 1)
        print()
        self.assertEqual(9, solution(6, [3, 4, 5, 5, 2]))
        print()
        self.assertEqual(11, solution(6, [3, 4, 5, 4, 2]))
        print()
        sol1 = solution(M=3, A=[1,2,1,2,1])
        print("sol1", sol1)

    def test_maximum_M(self):
        M = 100000
        A = [0] * 100000
        self.assertEqual(solution(M, A), 100000)