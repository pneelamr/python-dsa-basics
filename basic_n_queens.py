# N-Queens: Place N queens on an N×N chessboard so no two queens share a row, column, or diagonal.
# Solved with backtracking — place one queen per row, pruning positions attacked by earlier queens.
# Has N! upper bound on placements but pruning drastically reduces explored nodes in practice.

# Time: O(N!) — N choices for row 1, N-1 for row 2, etc. (pruning reduces this significantly)
# Space: O(N) — board array and recursion stack depth
def n_queens(n):
    solutions = []
    board = [-1] * n
    _solve(board, 0, n, solutions)
    return solutions


def _solve(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if _is_safe(board, row, col):
            board[row] = col
            _solve(board, row + 1, n, solutions)
            board[row] = -1


def _is_safe(board, row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True


def display(solution):
    n = len(solution)
    for row in range(n):
        print(' '.join('Q' if solution[row] == col else '.' for col in range(n)))
    print()
