# Time: O(M * N * 4^L) — M*N cells, 4 directions, L = word length
# Space: O(L) — recursion stack depth

def word_search(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'

        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
