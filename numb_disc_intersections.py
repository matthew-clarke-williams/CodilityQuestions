"""
# Number of Disc Intersections

Compute the number of intersections in a sequence of discs.

https://codility.com/programmers/task/number_of_disc_intersections/

## Problem Description

We draw N discs on a plane. The discs are numbered from 0 to N - 1. A zero-indexed array A of N non-negative
integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0)
and radius A[J].

We say that the J-th disc and K-th disc intersect if J <> K and the J-th and K-th discs have at least one common
point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

https://codility-frontend-prod.s3.amazonaws.com/media/task_static/number_of_disc_intersections/static/images/auto/0eed8918b13a735f4e396c9a87182a38.png

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of
intersecting discs. The function should return -1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.

---
In other words:
With every value in the array,
draw a circle with its center on the x-axis where the index lies,
and a radius of its value.
Count the number of intersections between all the circles.

## Solution

The brute-force solution visits every circle with every other circle.
It is: O(N**2) 50% (100% correct, 12% performance)
https://app.codility.com/demo/results/trainingYTV8B5-MTB/

The "fast" solution  considers where the openings and closings occur, but
abandons their individual pairings.  Thus, we have points on a line, which
are either an "opening" or a "closing" of a circle.  Sort the two lists then
step through all the "closing" points and count the number of "opening" points
which have not yet been closed.
Aside from the sort, O(log(N)), we can achieve the answer in single pass O(N).

 * collect all the "openings" and "closings" into two lists.
 * sort both lists
 * for every closing
    * for every opening between this closing and the last
      * mark an intersection
 * that's our answer

It is: O(N*log(N)) 100%.
https://app.codility.com/demo/results/trainingQKGBMA-DQ7/
"""
import itertools
import unittest

MAX_INTERSECTIONS = 10000000  # Runaway breakpoint.

def solution(A):
    # Create an array to store the start and end points of each disc
    start_points = []
    end_points = []
    for center, radius in enumerate(A):
        start_points.append(center - radius)
        end_points.append(center + radius)

    # Sort the start and end points
    start_points.sort()
    end_points.sort()

    intersections = 0  # Variable to store the count of intersections
    cur_num_intersecting = 0  # Variable to store the count of active discs
    start_index = 0

    for end_point in end_points:
        # Count the number of discs intersecting with the current end point
        while start_index < len(start_points) and start_points[start_index] <= end_point:
            start_index += 1
            cur_num_intersecting += 1

        # Decrement the count of active discs for the current end point
        cur_num_intersecting -= 1

        # Add the count of intersections for the current end point
        intersections += cur_num_intersecting

        if intersections > 10000000:  # Check for exceeding the limit
            return -1

    return intersections


A = [1, 5, 2, 1, 4, 0]
print(solution(A))  # Output should be 11


class TestExercise(unittest.TestCase):
    """
    example1: example test
    simple1
    simple2
    simple3
    extreme_small: empty and [10]
    small1
    small2
    small3
    overflow: arithmetic overflow tests
    medium1
    medium2
    medium3
    medium4
    10M_intersections: 10.000.000 intersections
    big1
    big2
    big3: [0]*100.000
    """

    def test_example(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)

    def test_simple(self):
        self.assertEqual(solution([1, 1, 1]), 3)  # this is not 5, but 3!

    def test_extreme_small(self):
        self.assertEqual(solution([]), 0)
        self.assertEqual(solution([10]), 0)
        self.assertEqual(solution([1, 1]), 1)

    def test_extreme_large(self):
        A = [10000000] * 100000
        self.assertEqual(solution(A), -1)
