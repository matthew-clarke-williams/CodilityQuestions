"""
Solve this problem in Python. Use comments in the code to clearly describe the steps and why each step is taken.
"""
import unittest


def check_at_edge(cur_pos, direction, N, M):
    """
    Checks if we are at an edge of the board in the direction we want to move

    N = num rows
    M = num cols

    Will return:
        False - if we CANNOT make the move
        TRUE - if we CAN make the move
    """
    # Check direction
    if direction == "U":
        if cur_pos[0] == 0:
            # Can't move up - stay where we are
            return False

        # Also can't move if object blocking path

    elif direction == "D":
        if cur_pos[0] == M - 1:
            # Can't move down - stay where we are
            return False

    elif direction == "L":
        if cur_pos[1] == 0:
            # Can't move left - stay where we are
            return False

    elif direction == "R":
        if cur_pos[0] == M - 1:
            # Can't move right - stay where we are
            return False

    # Otherwise, we have no WALL blocking our path
    return True


def update_cur_pos(cur_pos, direction):
    """
    Given the current position and assuming move is allowed, will update the current position
    """
    if direction == "U":
        new_pos = [cur_pos[0] - 1, cur_pos[1]]
    elif direction == "D":
        new_pos = [cur_pos[0] + 1, cur_pos[1]]
    elif direction == "L":
        new_pos = [cur_pos[0], cur_pos[1] - 1]
    elif direction == "R":
        new_pos = [cur_pos[0], cur_pos[1] + 1]

    return new_pos

def check_object(cur_pos, direction, board):
    """
    Given the current coordinates, will check if there is an object blocking our path

    Will return:
        False - if we CANNOT make the move (i.e. object blocking path)
        TRUE - if we CAN make the move  (i.e. object not blocking path)
    """

    new_pos = update_cur_pos(cur_pos=cur_pos, direction=direction)
    if board[new_pos[0]][new_pos[1]] == "#":
        # Move not allowed
        return False
    else:
        # new space is unoccupied "."
        return True


def solution(board, moves):
    """
    Returns the final coordinates of the character
    """
    # Firstly, K can be 0 so no moves will be made and coordinates will be [0, 0]
    if len(moves) == 0:
        return [0, 0]

    N = len(board)    # Number of rows
    M = len(board[0])    # Number of columns
    cur_pos = [0, 0]    # Initialise current position

    for direction in moves:
        # Check if we are not blocked by an edge or an object
        if check_at_edge(cur_pos=cur_pos, direction=direction, N=N, M=M):
            # We aren't blocked by a wall
            if check_object(cur_pos=cur_pos, direction=direction, board=board):
                # We aren't blocked by an object
                cur_pos = update_cur_pos(cur_pos=cur_pos, direction=direction)
            else:
                continue  # We are blocked by an object, go to next move
        else:
            continue

    return cur_pos

x = solution(["#..",".#."], "DLRR")
print(x)

class TestExercise(unittest.TestCase):
    """
    example: example test
    one_triple: three elements
    simple1: simple tests
    simple2: simple tests
    small_random: random small, length=100
    medium_range: -1000, -999,...,1000, length 1000 = 999000000
    medium_random: length ~10000
    large_random: random large, length 100000
    large_range: 2000 * (-10..10) + [-1000, 500, -1] = 5000000
    extreme_large: (-2, .., -2, 1, .., 1) and (MAX_INT)...(MAX_INT), length ~100000
    """
    def test_example(self):
        self.assertEqual(solution([".#.","..#"], "DLRR"), [1, 1])

    def test_one_by_one(self):
        self.assertEqual(solution(["."], "DLRR"), [0, 0])

    def test_zero_moves(self):
        self.assertEqual(solution([".#.","..#"], ""), [0, 0])
