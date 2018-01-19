"""Implement a queue with 2 stacks.  Queue should have enqueue and dequeue
methods and should be FIFO - first in first out."""


class Stack(object):
    """Stack class with push and pop methods."""

    def __init__(self):

        self.data = []

    def push(self, new_data):
        """Add new data to the top of Stack."""

        self.data.append(new_data)

    def stack_pop(self):
        """Pop and return top item from Stack."""

        return self.data.pop()


class Queue(object):
    """Queue with enqueue and dequeue methods - FIFO queue."""

    def __init__(self):

        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, new_data):
        """Add new item to end of Queue."""

        if not self.stack_1.data:
            self.stack_1.push(new_data)

        else:

            while self.stack_1.data:
                self.stack_2.push(self.stack_1.stack_pop())

            self.stack_1.push(new_data)

            while self.stack_2.data:
                self.stack_1.push(self.stack_2.stack_pop())

    def dequeue(self):
        """Pop and return first item from beginning of queue."""

        return self.stack_1.stack_pop()


example = Queue()
example.enqueue(1)
example.enqueue(2)
example.enqueue(3)
example.enqueue(4)

print example.stack_1.data
print example.dequeue()
