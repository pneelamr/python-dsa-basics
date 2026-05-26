class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self._size += 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError(f"index {index} out of range for list of size {self._size}")
        if index == 0:
            self.prepend(value)
            return
        node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        node.next = current.next
        current.next = node
        self._size += 1

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return " -> ".join(str(v) for v in self) + " -> None"
