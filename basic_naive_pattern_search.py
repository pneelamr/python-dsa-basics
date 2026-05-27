# Naive Pattern Search: Brute-force string matching that slides the pattern over the text one position at a time.
# At each position, compares the pattern character by character against the text.
# O(n × m) worst case; simple but inefficient for large inputs with many partial matches.

# Time: O(n*m) — for each of n positions checks up to m pattern characters
# Space: O(1) — only loop indices and matches list (output)
def naive_pattern_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches
