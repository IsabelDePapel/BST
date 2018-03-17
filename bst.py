"""Abstract class for a binary search tree."""


class BST:
    """Basic Binary Search Tree."""

    # TODO prevent BST from being instantiated
    def __init__(self):
        self._root = None

    @property
    def root(self):
        """Return the root of the tree."""
        raise NotImplementedError

    @root.setter
    def root(self, node):
        """Set the root of the tree."""
        raise NotImplementedError

    def search(self, value):
        """ Find given element in a BST."""
        raise NotImplementedError

    def insert(self, value):
        """
        Insert the given value into a BST.

        Values do not have to be unique and are always inserted at empty
        leaf nodes. Duplicate values are inserted in the left subtree.
        """
        raise NotImplementedError

    def height(self):
        """Calculate height of the tree."""
        raise NotImplementedError

    def pre_order(self):
        """Print out values of the tree in pre-order traversal (root,L,R)."""
        raise NotImplementedError

    def in_order(self):
        """Print out values of the tree in in-order traversal (L,root,R)."""
        raise NotImplementedError

    def post_order(self):
        """Print out values of the tree in post-order traversal (L,R,root)."""
        raise NotImplementedError
