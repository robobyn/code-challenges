"""Linked list challenge following URL paths."""

# work in progress from Python challenge site
import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="


class Node(object):
    """Node object for use in linked list."""

    def __init__(self, data, next=None):
        """Init method for instantiation of new Node.

           Next node defaults to None unless specified."""

        data = self.data
        next = self.next


def follow_next(head_node):
    """Track next node until destination reached."""

    depth = 0

    if depth > 400:
        return head_node
