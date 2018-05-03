class LinkedListNode(object):
    """A node object in a linked list."""

    def __init__(self, value):

        self.value = value
        self.next = None


def delete_node(node_object):
    """Given a variable pointing to a node to be deleted from a Linked List,
    delete that node from the Linked List.  Note - this function does NOT provide
    the head node to the linked list."""

    if not node_object.next:
        node_object = None

    else:
        next_value = node_object.next.value
        node_object.value = next_value

    if not node_object.next.next:
        node_object.next = None

    else:
        node_object.next = node_object.next.next


a = LinkedListNode("a")
b = LinkedListNode("b")
c = LinkedListNode("c")

a.next = b
b.next = c

delete_node(b)

print a.next.value
