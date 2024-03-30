"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""



def solution(A):
    """
    Given a non-empty array A consisting of N integers, returns the number of equi leaders.
    Uses Boyer-Moore Majority voting algorithm

    If there is an equileader, then it must also be the leader of the whole array too.
    """
    # Step 1: Find the majority leader of the array using the Boyer-Moore Voting Algorithm
    leader = None
    count = 0
    for num in A:
        if count == 0:
            leader = num
            count = 1
        elif leader == num:
            count += 1
        else:
            count -= 1

    # Step 2: Verify if the leader is actually a leader
    total_leader_count = A.count(leader)
    if total_leader_count <= len(A) // 2:
        return 0  # There is no leader in the array

    # Step 3: Count equi leaders
    num_EL = 0
    left_leader_count = 0
    for i in range(len(A)):
        if A[i] == leader:
            left_leader_count += 1
        if left_leader_count > (i + 1) // 2:
            # it is a leader of left side
            right_leader_count = total_leader_count - left_leader_count
            if right_leader_count > (len(A) - (i+1)) // 2:
                # it is also a leader on right side
                num_EL += 1

    return num_EL


# Test the function
A = [4, 3, 4, 4, 4, 2]
print(solution(A))  # Output should be 2

print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,2]))

