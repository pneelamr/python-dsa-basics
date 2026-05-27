# Time: O(n²) — expands around each of 2n-1 centers; each expansion up to O(n)
# Space: O(1) — only pointer variables and the result substring reference
def lps_expand(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ''
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest


# Time: O(n²) — fills n×n dp table checking all substrings of each length
# Space: O(n²) — dp boolean table of size n×n
def lps_dp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length

    return s[start:start + max_len]
