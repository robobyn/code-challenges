class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "<LinkedListNode value: {}>".format(self.value)


def find_kth_to_last_node(k, head_node):
    """Find and return the kth to the last node in a Linked List.

    Params: k is a positive int representing the position of the node to locate.
    head_node is the head of a linked list - must be type LinkedListNode.

    Returns: Node kth to last in linked list."""

    current = head_node
    counter = 0

    while current:
        counter += 1
        current = current.next

    if k > counter:
        return "There are fewer than {} nodes in this linked list.".format(k)

    target_idx = counter - k
    target_node = head_node
    second_counter = 0

    while second_counter < target_idx:
        second_counter += 1
        target_node = target_node.next

    return target_node


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print find_kth_to_last_node(2, a)
