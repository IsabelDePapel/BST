class Node:
    """Node class for bst class."""

    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None

    def __str__(self):
        s = "Node: "
        if self._value is None:
            s += "Empty"
        else:
            s += str(self._value)
        return s

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

        return self.__search_wrapper(self._root, value)

    def __search_wrapper(self, root, value):
        """Private wrapper method for insert."""
        if root is None:
            return False

        if root.value == value:
            return True
        elif value < root.value:
            return self.__search_wrapper(root.left, value)
        else:
            return self.__search_wrapper(root.right, value)

    def insert(self, value):
        """
        Insert the given value into a BST.

        Values do not have to be unique and are always inserted at empty
        leaf nodes. Duplicate values are inserted in the left subtree.

        Uses wrapper to avoid having to specify root when calling the function.
        """
        if self._root is None:
            self._root = Node(value)
            return

        return self.__insert_wrapper(self._root, value)

    def __insert_wrapper(self, root, value):
        """Private wrapper method for insert."""
        # search tree, and insert in L or R subtree
        if value <= root.value:
            if root.left is None:  # if leaf is empty
                root.left = Node(value)
                return
            return self.__insert_wrapper(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
                return
            return self.__insert_wrapper(root.right, value)

    def height(self):
        """Recursively calculate height of the tree."""
        return self.__height_wrapper(self._root)

    def __height_wrapper(self, root):
        if root is None:
            return 0

        left_height = self.__height_wrapper(root.left)
        right_height = self.__height_wrapper(root.right)

        return max([left_height, right_height]) + 1

    def pre_order(self):
        """Print out values of the tree in pre-order traversal (root,L,R)."""
        self.__pre_order_wrapper(self._root)

    def __pre_order_wrapper(self, root):
        if root is None:
            return

        print(root.value, end=' ')
        self.__pre_order_wrapper(root.left)
        self.__pre_order_wrapper(root.right)

    def in_order(self):
        """Print out values of the tree in in-order traversal (L,root,R)."""
        self.__in_order_wrapper(self._root)

    def __in_order_wrapper(self, root):
        if root is None:
            return

        self.__in_order_wrapper(root.left)
        print(root.value, end=' ')
        self.__in_order_wrapper(root.right)

    def post_order(self):
        """Print out values of the tree in post-order traversal (L,R,root)."""
        self.__post_order_wrapper(self._root)

    def __post_order_wrapper(self, root):
        if root is None:
            return

        self.__post_order_wrapper(root.left)
        self.__post_order_wrapper(root.right)
        print(root.value, end=' ')


tree = BST()
tree.insert(4)
tree.insert(5)
tree.insert(2)
tree.insert(3)

# pre should print out: 4 2 3 5
tree.pre_order()
print('\n')
# in should print out: 2 3 4 5
tree.in_order()
print('\n')
# post should print out: 3 2 5 4
tree.post_order()
print('\n')
