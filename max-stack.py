"""Use stack class to implement a new class 'MaxStack' with a method 'get_max()'
that returns the largest element in the stack.  Stacks will contain only
integers."""


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""

        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):

    def max_push(self, new_data):
        """Push data to top of MaxStack."""

        if not self.items:
            self.push(new_data)

        elif new_data >= self.items[-1]:
            self.push(new_data)

        else:
            temp = self.pop()
            self.push(new_data)
            self.push(temp)

    def get_max(self):
        """Return, but do not remove, the largest item in MaxStack."""

        return self.peek()


example = MaxStack()
example.max_push(9)
example.max_push(4)
example.max_push(12)
example.pop()
example.max_push(5)
example.max_push(2)
example.pop()
example.max_push(18)
example.pop()

print example.items
print example.get_max()
