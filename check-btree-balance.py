"""Given a node in a binary search tree check to see if the tree is
'superbalanced.' A tree is superbalanced if each leaf node's depth is no more
than one degree off from each other leaf node's depth."""


class B_Tree_Node(object):
    """Binary tree node class."""

    def __init__(self, value):
        """Method for instantiating binary tree node."""

        self.value = value
        self.left = None
        self.right = None


def check_tree_balance(binary_node):
    """Check binary tree to see if it is superbalanced.

    In: Object of B_Tree_Node class.

    Return Value: Boolean."""

    node_stack = [(binary_node, 0)]
    depths = []

    while node_stack:

        next_node = node_stack.pop()
        current = next_node[0]
        depth = next_node[1]

        if current.left is None and current.right is None:

            if depth not in depths:
                depths.append(depth)

                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] -
                                                                depths[1]) > 1):
                    return False

        else:
            if current.left:
                node_stack.append((current.left, depth + 1))

            if current.right:
                node_stack.append((current.right, depth + 1))

    return True


root_node = B_Tree_Node(8)
six = B_Tree_Node(6)
ten = B_Tree_Node(10)
four = B_Tree_Node(4)
nine = B_Tree_Node(9)
seven = B_Tree_Node(7)
eleven = B_Tree_Node(11)

root_node.left = six
root_node.right = ten
six.left = four
six.right = seven
ten.left = nine
ten.right = eleven

print check_tree_balance(root_node)

unbalanced = B_Tree_Node(10)
five = B_Tree_Node(5)
three = B_Tree_Node(3)
two = B_Tree_Node(2)

unbalanced.left = five
five.left = three
three.left = two

print check_tree_balance(unbalanced)
