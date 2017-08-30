class Stack(object):
    """LIFO stack - has access to push & pop methods."""

    def __init__(self, data=[]):
        """Method for instantiating a Stack object on a Python list.

           Data should be in Python list format."""

        self.data = data

    def stack_push(self, item):
        """Method for adding item to the top of Stack."""

        self.data.append(item)

    def stack_pop(self):
        """Method for popping and returning top item from Stack."""

        top_item = self.data.pop()
        return top_item


class Queue(object):
    """FIFO queue object - built with two Stack objects."""

    def __init__(self, stack_1):
        """Method for instantiating a Queue object with 2 Stack objects.

           Args: stack_1 should contain data to be enqueued and dequeued.
                 stack_2 should be empty for methods to work."""

        self.stack_1 = stack_1
        self.stack_2 = Stack()

    def enqueue(self, item):
        """Method for adding a new item to end of Queue."""

        self.stack_1.stack_push(item)

    def dequeue(self):
        """Method for removing and returning 1st item in Queue."""

        # while there are still items in 1st stack
        while len(self.stack_1.data) > 0:

            top_item = self.stack_1.stack_pop()
            self.stack_2.stack_push(top_item)

        first_in_queue = self.stack_2.stack_pop()

        while len(self.stack_2.data) > 0:

            top_item = self.stack_2.stack_pop()
            self.stack_1.stack_push(top_item)

        return first_in_queue


numbers = Stack([1, 2, 3, 4])

a_queue = Queue(numbers)
