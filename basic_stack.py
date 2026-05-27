# Time: O(1) — push and pop are both constant time operations
# Space: O(1) — no extra space per operation (overall stack is O(n))
def push(stack, value):
    stack.append(value)


def pop(stack):
    if is_empty(stack):
        raise IndexError("pop from empty stack")
    return stack.pop()


def peek(stack):
    if is_empty(stack):
        raise IndexError("peek from empty stack")
    return stack[-1]


def is_empty(stack):
    return len(stack) == 0


def display(stack):
    print(stack)
