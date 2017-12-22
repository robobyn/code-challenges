"""Find the 2nd largest element in a binary search tree."""


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


def find_largest_element(root_node):
    """Function to find largest element in BST given root node.

    Input: root_node should be from B_Tree_Node class.
    Function assumes BST is valid and properly ordered.

    Returns: Node with largest value in BST."""

    current = root_node

    while current.right:
        current = current.right

    return current


def find_2nd_largest_element(b_tree_node):
    """Function to find 2nd largest element in a BST.

    Input: b_tree_node should be root node of BST from B_Tree_Node class.
    Function assumes binary tree is valid and in correct order.

    Returns: Node with 2nd largest value in tree."""

    current = b_tree_node

    # loop unless current node is None
    while current:

        # if there is no right node but there is a left node in the tree
        # 2nd largest element will be the largest element of the left tree
        if current.left and not current.right:

            return find_largest_element(current.left)

        # if current has a right node that is a leaf
        # then current is the second largest element of tree
        if current.right and not current.right.left and not current.right.right:
            return current

        # keep going right until 2nd largest element found
        # no need to traverse entire tree if BST structured properly
        current = current.right

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

print find_largest_element(root_node).value
print find_2nd_largest_element(root_node).value

unbalanced = B_Tree_Node(10)
five = B_Tree_Node(5)
six = B_Tree_Node(6)
two = B_Tree_Node(2)

unbalanced.left = five
five.right = six
five.left = two

print find_largest_element(unbalanced).value
print find_2nd_largest_element(unbalanced).value
