# Time: O(n) — slice creates reversed copy then compares character by character
# Space: O(n) — reversed slice creates a new string of length n
def is_palindrome(s):
    return s == s[::-1]


# Time: O(n) — two pointers converge from both ends comparing n/2 pairs
# Space: O(1) — only two index variables used
def is_palindrome_two_pointer(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_ignore_non_alpha(s):
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]
