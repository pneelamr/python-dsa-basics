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
