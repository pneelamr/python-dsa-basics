# Time: O(2^(N^2)) — each cell has 2 choices (move or not), N^2 cells
# Space: O(N^2) — solution matrix and recursion stack

def rat_in_maze(maze):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]
    paths = []
    _solve(maze, 0, 0, n, solution, paths, '')
    return paths


def _solve(maze, row, col, n, solution, paths, path):
    if row == n - 1 and col == n - 1 and maze[row][col] == 1:
        paths.append(path)
        return

    if _is_safe(maze, row, col, n, solution):
        solution[row][col] = 1

        _solve(maze, row + 1, col, n, solution, paths, path + 'D')
        _solve(maze, row, col + 1, n, solution, paths, path + 'R')
        _solve(maze, row - 1, col, n, solution, paths, path + 'U')
        _solve(maze, row, col - 1, n, solution, paths, path + 'L')

        solution[row][col] = 0


def _is_safe(maze, row, col, n, solution):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == 1 and solution[row][col] == 0


def display(maze, path):
    n = len(maze)
    solution = [[0] * n for _ in range(n)]
    row, col = 0, 0
    solution[0][0] = 1
    for move in path:
        if move == 'D': row += 1
        elif move == 'R': col += 1
        elif move == 'U': row -= 1
        elif move == 'L': col -= 1
        solution[row][col] = 1
    for r in solution:
        print(' '.join('1' if c else '.' for c in r))
    print()
