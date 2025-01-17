"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1

    if countX > countO:
        return O
    else:
        return X

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allposibleactions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
           if board[row][col] == EMPTY:
                allposibleactions.add((row, col))
    return allposibleactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a valid action")
    
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


def check_row(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_col(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def check_first_diag(board, player):
    count = 0
    for row in range(len(board)):
        if board[row][row] == player:
            count += 1
    return count == 3


def check_second_diag(board, player):
    count = 0
    for row in range(len(board)):
        if board[row][len(board) - row - 1] == player:
            count += 1
    return count == 3


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_row(board, X) or check_col(board, X) or check_first_diag(board, X) or check_second_diag(board, X):
        return X
    elif check_row(board, O) or check_col(board, O) or check_first_diag(board, O) or check_second_diag(board, O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    v = -math.inf
    
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    optimal_action = None

    if player(board) == X:
        best_value = -math.inf
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                optimal_action = action

    elif player(board) == O:
        best_value = math.inf
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                optimal_action = action

    return optimal_action