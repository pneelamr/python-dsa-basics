class StaticArray:
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def append(self, value):
        if self._size == self._capacity:
            raise OverflowError("array is full")
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if self._size == self._capacity:
            raise OverflowError("array is full")
        if index < 0 or index > self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1

    def find(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        return self._data[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        self._data[index] = value

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def __repr__(self):
        filled = self._data[:self._size]
        empty = ["_"] * (self._capacity - self._size)
        return "[" + ", ".join(str(v) for v in filled + empty) + f"] (size={self._size}, capacity={self._capacity})"
