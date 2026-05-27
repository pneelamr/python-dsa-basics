# Time: O(8^(N^2)) — 8 moves per cell, N^2 cells
# Space: O(N^2) — board and recursion stack

MOVES = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]


def knights_tour(n, start_row=0, start_col=0):
    board = [[-1] * n for _ in range(n)]
    board[start_row][start_col] = 0

    if _solve(board, start_row, start_col, 1, n):
        return board
    return []


def _solve(board, row, col, move_num, n):
    if move_num == n * n:
        return True

    for dr, dc in _sort_by_onward(board, row, col, n):
        next_row, next_col = row + dr, col + dc
        board[next_row][next_col] = move_num
        if _solve(board, next_row, next_col, move_num + 1, n):
            return True
        board[next_row][next_col] = -1

    return False


def _sort_by_onward(board, row, col, n):
    moves = []
    for dr, dc in MOVES:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == -1:
            onward = sum(1 for ddr, ddc in MOVES
                         if 0 <= r+ddr < n and 0 <= c+ddc < n and board[r+ddr][c+ddc] == -1)
            moves.append((onward, dr, dc))
    return [(dr, dc) for _, dr, dc in sorted(moves)]


def display(board):
    n = len(board)
    for row in board:
        print(' '.join(f'{v:>3}' for v in row))
