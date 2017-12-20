"""Check to see if BST is valid - each node's value is greater than all values
in its left substree and less than all values in the right subtree."""


class B_Tree_Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = B_Tree_Node(value)
        return self.left

    def insert_right(self, value):
        self.right = B_Tree_Node(value)
        return self.right


def is_valid_tree(b_tree_node):
    """Check binary tree to ensure it is a valid binary search tree.

    Params: b_tree_node should be the root node of a binary tree of
    BinaryTreeNode class.

    Returns: Boolean."""

    # start a stack with root node of tree
    # use stack to keep track of nodes that need to be checked
    # along with arbitrarily low and arbitrarily high value to initiate
    # upper and lower bound of valid values possible for node
    nodes = [(b_tree_node, -float('inf'), float('inf'))]

    while nodes:

        current, lower_bound, upper_bound = nodes.pop()

        if current.value <= lower_bound or current.value >= upper_bound:
            return False

        if current.left:
            # to be valid, left node value must be between current lower bound
            # and the value of the current node
            nodes.append((current.left, lower_bound, current.value))

        if current.right:
            # to be valid, right node value must be between current node's value
            # and current upper bound
            nodes.append((current.right, current.value, upper_bound))

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

print is_valid_tree(root_node)

root_node = B_Tree_Node(8)
six = B_Tree_Node(6)
ten = B_Tree_Node(10)
four = B_Tree_Node(4)
nine = B_Tree_Node(9)
seven = B_Tree_Node(7)
eleven = B_Tree_Node(11)

root_node.left = six
root_node.right = four
six.left = ten
six.right = seven
ten.left = nine
ten.right = eleven

print is_valid_tree(root_node)
