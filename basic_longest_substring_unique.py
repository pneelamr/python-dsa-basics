# Sliding Window (Variable): Expand and shrink a window dynamically to satisfy a constraint.
# A set or dict tracks the window's contents; shrink from the left when the constraint is violated.
# Used for longest substring without repeating characters, most k distinct chars, and minimum window substrings.

# Time: O(n) — each character is added and removed from the set at most once
# Space: O(min(n, a)) — set holds at most min(n, alphabet_size) characters
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Time: O(n) — each character enters and leaves the window dict at most once
# Space: O(k) — dict holds at most k+1 distinct characters at any point
def longest_with_k_distinct(s, k):
    char_count = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        char_count[ch] = char_count.get(ch, 0) + 1
        while len(char_count) > k:
            left_ch = s[left]
            char_count[left_ch] -= 1
            if char_count[left_ch] == 0:
                del char_count[left_ch]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Time: O(|s| + |t|) — each character in s is added/removed from the window at most once
# Space: O(|t|) — frequency maps for t and the current window
def min_window_substring(s, t):
    if not t or not s:
        return ''
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    have = {}
    formed = 0
    required = len(need)
    left = 0
    min_len = float('inf')
    min_left = 0
    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1
    return '' if min_len == float('inf') else s[min_left:min_left + min_len]
