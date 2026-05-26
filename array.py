import ctypes


class Array:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._data = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_data = self._make_array(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError(f"index {index} out of range for array of size {self._size}")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if self._size < self._capacity // 4 and self._capacity > 1:
            self._resize(self._capacity // 2)

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
        return "[" + ", ".join(str(self._data[i]) for i in range(self._size)) + "]"
