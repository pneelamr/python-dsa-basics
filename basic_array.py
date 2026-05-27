# Array: Fixed-size sequential collection of elements accessed by index in O(1).
# Backed by a Python list with a fixed capacity enforced at insert time.
# Supports append, insert, delete, search, and in-place reversal.

# Time: O(1) — appending to end of list is amortized constant time
# Space: O(1) — no extra space needed (overall array structure is O(n))
def append(arr, value):
    arr += [value]


def insert(arr, index, value):
    arr.insert(index, value)


def delete(arr, index):
    arr.pop(index)


def find(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


def get(arr, index):
    return arr[index]


def set_val(arr, index, value):
    arr[index] = value


def display(arr):
    print(arr)
