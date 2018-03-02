class Node:
    """Node class for bst class."""

    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None

    @property
    def value(self):
        return self._value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node


class BST:

    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def search(self, value):
        """
        Find given element in a BST.

        Uses wrapper to avoid having to specify root when calling the function.
        """
        def search_wrapper(root, value):
            if not root:
                return False

            if root.value == value:
                return True
            elif root.value < value:
                return search_wrapper(root.left, value)
            else:
                return search_wrapper(root.right, value)

        return search_wrapper(self._root, value)

    def insert(self, value):
        if not self._root:
            self._root = Node(value)
            
