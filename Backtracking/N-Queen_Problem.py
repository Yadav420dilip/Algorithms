N = 4  # Dimension of the board


# To check the current cell is safe or not to place the queen
def is_safe(board, row, col):
    # Always check  left side because you approaching from left to right there is no any element on the right therefore no need to check
    for i in range(col):  # Check left side of the current cell
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):  # Check the left upper diagonal
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):  # Check the left lower diagonal
        if board[i][j] == 1:
            return False

    return True


def check_solution(board, col):
    if col >= N:  # If the col exceeding the dimension means you check all the possible cell
        return True

    for row in range(N):
        if is_safe(board, row, col):  # Check if the cell is safe or not
            board[row][col] = 1
            if check_solution(board,
                              col + 1):  # On the successful the place of the queen call the function by increasing column by 1
                return True
            board[row][col] = 0  # if not then revert back
    return False


chess_board = [[0 for _ in range(N)] for _ in range(N)]
if not check_solution(chess_board, 0):
    print("No solution exist")

print(chess_board)
