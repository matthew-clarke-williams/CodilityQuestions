"""
# StoneWall - Cover "Manhattan skyline" using the minimum number of rectangles."

https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant;
however, it should have different heights in different places. The height of the wall is specified by an array H of N
positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular,
H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular).
Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

    def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:
  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8

the function should return 7. The figure shows one possible arrangement of seven blocks.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array H is an integer within the range [1..1,000,000,000].
"""

import unittest

def solution(H):
    stack = []  # Initialize an empty stack to keep track of heights
    blocks = 0  # Initialize the number of blocks needed

    for height in H:
        # Remove all blocks that are taller than the current height
        while len(stack) > 0 and stack[-1] > height:
            stack.pop()

        # If the stack is empty or the current height is taller than the top block
        if len(stack) == 0 or height > stack[-1]:
            blocks += 1  # Add a new block
            stack.append(height)  # Add the current height to the stack

    return blocks


# Example usage:
H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))


class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]), 7)








