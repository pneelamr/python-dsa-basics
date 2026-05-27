# String Reversal: Reversing the characters of a string or the words within a sentence.
# Python strings are immutable so reversal returns a new string; character lists can be reversed in-place.
# Includes reverse_string (slice), reverse_words (split + reverse), and reverse_in_place (two-pointer).

# Time: O(n) — creates a reversed copy of the string character by character
# Space: O(n) — new string of length n allocated for the result
def reverse_string(s):
    return s[::-1]


def reverse_words(s):
    return ' '.join(s.split()[::-1])


def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
