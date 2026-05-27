# Sudoku Solver: Fill a partially completed 9×9 grid so every row, column, and 3×3 box contains digits 1–9 exactly once.
# Uses backtracking — find the next empty cell, try digits 1–9, recurse; undo on failure.
# Constraint checking (row, col, box) prunes invalid placements before recursing.

# Time: O(9^m) — m is number of empty cells, 9 choices per cell
# Space: O(m) — recursion stack depth equals number of empty cells
def solve_sudoku(board):
    empty = _find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if _is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def _find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def _is_safe(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(9)]:
        return False
    box_r, box_c = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if board[r][c] == num:
                return False
    return True


def display(board):
    for r in range(9):
        row = ''
        for c in range(9):
            row += str(board[r][c]) + ' '
            if c in (2, 5):
                row += '| '
        print(row)
        if r in (2, 5):
            print('-' * 22)
