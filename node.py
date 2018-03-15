"""Node class for use in BST classes, both recursive and iterative."""

class Node:
    """Basic node class with left and right children."""

    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None

    def __str__(self):
        str_node = "Node: "
        if self._value is None:
            str_node += "Empty"
        else:
            str_node += str(self._value)
        return str_node

    @property
    def value(self):
        """Return value."""
        return self._value

    @property
    def right(self):
        """Return right child node."""
        return self._right

    @right.setter
    def right(self, node):
        """Set right child node."""
        self._right = node

    @property
    def left(self):
        """Return left child node."""
        return self._left

    @left.setter
    def left(self, node):
        """Set left child node."""
        self._left = node
