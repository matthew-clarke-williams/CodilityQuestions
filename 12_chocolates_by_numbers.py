"""
ChocolatesByNumbers - There are N chocolates in a circle. Count the number of chocolates you will eat.

Two positive integers N and M are given.
Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates.
After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0.
Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.
More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:
    def solution(N, M)
that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:
        N and M are integers within the range [1..1,000,000,000].
"""
import unittest

def solution(N, M):
    chocs_eaten = set()
    num_chocs_attempted = 0

    cur_choc = 0   # The position of the current chocolate
    # eat the first chocolate
    chocs_eaten.add(cur_choc)
    num_chocs_attempted += 1

    while len(chocs_eaten) == num_chocs_attempted:
        # move to next position
        cur_choc = (cur_choc + M) % N

        # Add the chocolate and see if the set size increases
        chocs_eaten.add(cur_choc)
        num_chocs_attempted += 1

    return len(chocs_eaten)

# Example usage
N = 100
M = 3
print(solution(N, M))  # Output should be 5


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution(10, 4), 5)
        self.assertEqual(solution(1,1), 1)
        self.assertEqual(solution(12,2), 6)
        self.assertEqual(solution(12, 13), 12)
        self.assertEqual(solution(50, 50), 1)
        self.assertEqual(solution(50, 1), 50)
        self.assertEqual(solution(50, 51), 50)
        self.assertEqual(solution(50, 49), 50)
        self.assertEqual(solution(50, 2), 25)
        self.assertEqual(solution(50, 48), 25)
        self.assertEqual(solution(50, 3), 50)
        self.assertEqual(solution(50, 47), 50)
        self.assertEqual(solution(50, 4), 25)
        self.assertEqual(solution(50, 46), 25)
        self.assertEqual(solution(50, 5), 10)
        self.assertEqual(solution(50, 45), 10)

