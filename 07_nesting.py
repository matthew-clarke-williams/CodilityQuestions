"""
# Nesting
https://app.codility.com/programmers/lessons/7-stacks_and_queues/nesting/

A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S is made only of the characters '(' and/or ')'.

Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
#---------------
# Solution
This is exactly the same problem and solution as "L7_Brackets", so I just cut/pasted
that solution and it worked perfectly.

Loop over the incoming chars.
If we get an opening bracket, push the closing bracket on to a stack.
If we get a closing bracket pop one off the stack, if it doesn't match: fail.
If we get a closing bracket and the stack is empty: fail.
If the string ends and the stack is empty: success.
O(N) https://app.codility.com/demo/results/trainingFVQXB8-TZB/
"""

import unittest

def solution(S):
    """
    Since the string, S can only be made of the characters: '(' and ')', it needs to
    have an even length if it is nested
    """
    # First if the length of the sting length is even
    if len(S) % 2 != 0:
        return 0    # String is not nested

    opening_brackets = []
    for element in S:
        if element not in ['(', ')']:
            return 0
        if element == '(':
            opening_brackets.append(element)
        else:
            # If there are no open brackets in the list, S isn't nested
            if not opening_brackets:
                return 0
            else:
                opening_brackets.pop()  # remove the last opening bracket

    if len(opening_brackets) == 0:
        return 1
    else:
        return 0

S = "(()(())())"
x = solution(S)

class TestExercise(unittest.TestCase):
    """
    """
    def test_examples(self):
        self.assertEqual(solution("())"), 0)
        self.assertEqual(solution("(()(())())"), 1)
