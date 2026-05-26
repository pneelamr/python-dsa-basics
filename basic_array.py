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
