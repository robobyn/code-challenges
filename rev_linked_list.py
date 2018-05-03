class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "<LinkedListNode value: {}>".format(self.value)


def reverse_ll(head_node):
    """Reverse linked list in place.

    Params: head_node must be LinkedListNode class object.

    Returns: New head of Linked List after reversal."""

    if type(head_node) != LinkedListNode:
        raise TypeError("head_node must be an object of LinkedListNode class.")

    if not head_node.next:
        return head_node

    current = head_node
    prev_node = None

    while current:
        temp = current.next
        current.next = prev_node
        prev_node = current
        current = temp

    return prev_node


ten = LinkedListNode(10)
nine = LinkedListNode(9)
eight = LinkedListNode(8)
seven = LinkedListNode(7)

ten.next = nine
nine.next = eight
eight.next = seven

single_node = LinkedListNode("All by myself")

print reverse_ll(ten).value
# print reverse_ll("not a node")
print reverse_ll(single_node).value
