"""
# GenomicRangeQuery

Find the minimal nucleotide from a range of sequence DNA.

## Problem Description

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which
correspond to the types of successive nucleotides in the sequence. Each nucleotide has an _impact
factor_, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4,
respectively. You are going to answer several queries of the form: What is the minimal impact factor of
nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The
K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the
DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
        whose impact factors are 3 and 2 respectively, so the answer is 2.

        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor
        is 4, so the answer is 4.

        The part between positions 0 and 6 (the whole string) contains all nucleotides, in
        particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q
consisting of M integers, returns an array consisting of M integers specifying the consecutive answers
to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P and Q is an integer within the range [0..N - 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.
"""
import unittest
import random

def solution(S, P, Q):
    impact_factor_dict = {"A": 1, "C": 2, "G": 3, "T": 4}

    results = []


    for index in range(len(P)):
        subsequence = S[P[index]: Q[index]+1]
        subsequence_set = set(subsequence)

        min_impact_factor = float('inf')
        for value in subsequence_set:
            if impact_factor_dict[value] < min_impact_factor:
                min_impact_factor = impact_factor_dict[value]
        results.append(min_impact_factor)

    return results

S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]

test = solution(S=S, P=P, Q=Q)


# maximum number of neucleotides in a sequence
MAX_N = 100000
# maximum number of queries
MAX_M = 50000

# impact factor of each neucleotide
IMPACT = {"A": 1, "C": 2, "G": 3, "T": 4}


class TestExercise(unittest.TestCase):
    """
    example: example test
    extreme_sinlge: single character string
    extreme_double: double character string
    simple: simple tests
    small_length_string: small length simple string
    small_random: small random string, length = ~300
    almost_all_same_letters: GGGGGG..??..GGGGGG..??..GGGGGG
    large_random: large random string, length
    extreme_large: all max ranges
    """
    def test_example(self):
        self.assertEqual(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]), [2, 4, 1])

    def test_random(self):
        seq = [random.choice("ACGT") for _ in range(1, 5000)]
        P_array, Q_array = [], []
        for _ in range(0, len(seq)):
            P = random.randint(0, len(seq) - 1)
            Q = random.randint(P, len(seq) - 1)
            P_array.append(P)
            Q_array.append(Q)
        solution(seq, P_array, Q_array)

    def test_extreme(self):
        S = "T" * MAX_N
        P = [0] * MAX_M
        Q = [MAX_N - 1] * MAX_M
        self.assertEqual(solution(S, P, Q), [4] * MAX_M)


