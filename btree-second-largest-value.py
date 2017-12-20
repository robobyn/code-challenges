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


def find_2nd_largest_element(b_tree_node):
    """Function to find 2nd largest element in a BST.

    Input: b_tree_node should be root node of BST from B_Tree_Node class.
    Function assumes binary tree is valid and in correct order.

    Returns: value of node with 2nd largest value in tree."""

    # assume root is largest value until larger value encountered
    largest = b_tree_node
    # assume value to the left of root is 2nd largest until larger val found
    second_largest = b_tree_node.left

    current = b_tree_node

    # loop as long as there is a node larger than current largest
    while current.right:

        second_largest = largest
        largest = current.right
        current = current.right

    return second_largest.value

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

print find_2nd_largest_element(root_node)

unbalanced = B_Tree_Node(10)
five = B_Tree_Node(5)
three = B_Tree_Node(3)
two = B_Tree_Node(2)

unbalanced.left = five
five.left = three
three.left = two

print find_2nd_largest_element(unbalanced)
