# create a balanced binary search tree from a sorted python list
# find center of list using len
# make mid be the root
# left will be all nodes to the left of mid recursively
# right will be all nodes to the right of mid recursively


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_bst(sorted_nums):
    """Make a balanced binary tree given sorted list of numbers."""

    mid = len(sorted_nums) / 2
    root = BinaryNode(sorted_nums[mid])
    left = sorted_nums[:mid]
    right = sorted_nums[(mid + 1):]

    if left:
        root.left = make_bst(left)

    if right:
        root.right = make_bst(right)

    return root


bst_root = make_bst([1, 2, 3, 4, 5, 6, 7])
even_length_bst_root = make_bst([1, 3, 6, 8, 10, 14])
