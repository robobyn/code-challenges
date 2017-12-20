# Append a child to a node in a Binary Search Tree

# create new node containing new data
# check if new node data greater than or less than root
# if greater than go right
# if less than go left
# continue until left is None if less than current node
# continue until right is None if greater than current node


class Node(object):

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):
        """A method to add a new node to Binary Search Tree."""

        new_node = Node(new_data)
        current = self

        while True:

            if new_data > current.data:

                if current.right is not None:
                    current = current.right

                else:
                    current.right = new_node
                    current = current.right
                    return "Success!"

            elif new_data < current.data:

                if current.left is not None:
                    current = current.left

                else:
                    current.left = new_node
                    current = current.left
                    return "Success!"

    def insert_recurse(self, new_data):
        """Same method as above using recursion."""

        if new_data >= self.data:

            if self.right is None:
                self.right = Node(new_data)
                print "Success"

            else:
                self.right.insert_recurse(new_data)

        else:

            if self.left is None:
                self.left = Node(new_data)
                print "Success"

            else:
                self.left.insert_recurse(new_data)


# build balanced tree to append child to
b_tree = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), Node(8)))

print b_tree.insert_recurse(0)
print b_tree.insert_recurse(9)
