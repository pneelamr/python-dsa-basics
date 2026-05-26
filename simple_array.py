def create(capacity):
    return {"data": [None] * capacity, "size": 0, "capacity": capacity}


def append(arr, value):
    if arr["size"] == arr["capacity"]:
        raise OverflowError("array is full")
    arr["data"][arr["size"]] = value
    arr["size"] += 1


def insert(arr, index, value):
    if arr["size"] == arr["capacity"]:
        raise OverflowError("array is full")
    if index < 0 or index > arr["size"]:
        raise IndexError(f"index {index} out of range")
    for i in range(arr["size"], index, -1):
        arr["data"][i] = arr["data"][i - 1]
    arr["data"][index] = value
    arr["size"] += 1


def delete(arr, index):
    if index < 0 or index >= arr["size"]:
        raise IndexError(f"index {index} out of range")
    for i in range(index, arr["size"] - 1):
        arr["data"][i] = arr["data"][i + 1]
    arr["data"][arr["size"] - 1] = None
    arr["size"] -= 1


def get(arr, index):
    if index < 0 or index >= arr["size"]:
        raise IndexError(f"index {index} out of range")
    return arr["data"][index]


def set_val(arr, index, value):
    if index < 0 or index >= arr["size"]:
        raise IndexError(f"index {index} out of range")
    arr["data"][index] = value


def find(arr, value):
    for i in range(arr["size"]):
        if arr["data"][i] == value:
            return i
    return -1


def display(arr):
    filled = arr["data"][:arr["size"]]
    empty = ["_"] * (arr["capacity"] - arr["size"])
    print("[" + ", ".join(str(v) for v in filled + empty) + f"] (size={arr['size']}, capacity={arr['capacity']})")
