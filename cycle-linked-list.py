"""Interview cake practice question re: linked lists and cycles."""


class LinkedListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def contains_cycle(head_node):
    """Returns boolean indicating whether singly linked list contains cycle.

       Args: Takes the first node of a singly linked list as input.  Node must
       be of the LinkedListNode class.

       Returns:  Boolean - True if linked list contains a cycle.  Cycle
       occurs when a node's 'next' attribute points back to a previous node
       in the list."""

    current = head_node
    seen = set()

    while current is not None:

        if current.value in seen:
            return True

        else:
            seen.add(current.value)
            current = current.next

    return False


def contains_cycle_constant_space(head_node):
    """Same as contains_cycle function but uses O(1) space."""

    # track two nodes traversing linked list at different speeds
    current = head_node
    control = head_node

    # while condition checks to see if there are zero or one nodes in list
    # if zero or one nodes in linked list there is no cycle
    while current is not None and current.next is not None:

        current = current.next.next
        control = control.next

        # if there is a cycle current and control will eventually catch up
        # with each other and function will return True
        if current is control:
            return True

    return False


beer = LinkedListNode("beer")
fries = LinkedListNode("fries")
burger = LinkedListNode("burger")
shake = LinkedListNode("shake")
cake = LinkedListNode("cake")

beer.next = fries
fries.next = burger
burger.next = shake
shake.next = cake

print contains_cycle(beer)
print contains_cycle_constant_space(beer)
