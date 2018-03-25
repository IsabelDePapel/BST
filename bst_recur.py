"""Implement Binary Search Tree abstract class using recursive methods."""

import node
from bst import BST


class RecursiveBST(BST):
    """Recursive Binary Search Tree."""

    def search(self, value):
        """Find given element in a BST."""
        return self.__search_wrapper(self._root, value)

    def __search_wrapper(self, current, value):
        """Private wrapper method for search."""
        if current is None:  # value not found
            return False
        elif value < current.value:
            return self.__search_wrapper(current.left, value)
        elif value > current.value:
            return self.__search_wrapper(current.right, value)

        # value found
        return True

    def insert(self, value):
        """
        Insert the given value into a BST.

        Values do not have to be unique and are always inserted at empty
        leaf nodes. Duplicate values are inserted in the left subtree.
        """
        # if tree is empty
        if self._root is None:
            self._root = node.Node(value)
            return
        
        return self.__insert_wrapper(self._root, value)

    def __insert_wrapper(self, current, value):
        """Private wrapper method for insert."""
        if value <= current.value:  # insert into left subtree
            # check if current has children
            if current.left is None:
                current.left = node.Node(value)
            else:
                return self.__insert_wrapper(current.left, value)
        else:
            if current.right is None:
                current.right = node.Node(value)
            else:
                return self.__insert_wrapper(current.right, value)

    def height(self):
        """Calculate height of the tree."""
        return self.__height_wrapper(self._root)

    def __height_wrapper(self, current):
        """Private wrapper method for height."""
        if current is None:
            return 0

        left = self.__height_wrapper(current.left)
        right = self.__height_wrapper(current.right)

        return max(left, right) + 1

    def min(self):
        """Return minimum value of binary tree."""
        # if self._root is None:
        #     return None

        return self.__min_wrapper(self._root)

    def __min_wrapper(self, current, current_min=None):
        """Private wrapper method for min."""
        if current is None:
            return current_min

        # min is leftmost leaf node
        return self.__min_wrapper(current.left, current.value)

    def delete(self, value):
        """
        Delete the given value from the tree.

        Raises error if value is not found.
        """
        return self.__delete_wrapper(self._root, value)

    def __delete_wrapper(self, current, value, parent=None):
        """
        Private wrapper method for delete.
        
        Keeps tracks of parent node.
        """
        if current is None:
            raise IndexError('value not found')
        elif value < current.value:
            return self.__delete_wrapper(current.left, value, current)
        elif value > current.value:
            return self.__delete_wrapper(current.right, value, current)

        # value found
        if current.left is None:  # one or no children
            current = current.right
        elif current.right is None:
            current = current.left
        else:  # 2 children
            # find in-order successor and set new value
            successor = self.__min_wrapper(current.right)

            current._value = successor

            # delete value starting from the subtree
            self.__delete_wrapper(current.right, successor, current)

        # if replacing root
        if parent is None:
            self._root = current
        # else point parent to new child
        # attach new child to where old node was
        else:
            if value < parent.value:
                parent.left = current
            else:
                parent.right = current

    def delete2(self, value):
        """
        Delete the given value from the tree. Returns root of tree.

        Returns None if value not found.
        """
        return self.__delete_wrapper2(self._root, value)

    def __delete_wrapper2(self, current, value):
        """
        Private method wrapper for delete.

        Returns new root node instead of tracking parent.
        WON'T RAISE ERROR if value not found.
        """
        if current is None:  # value not found
            return None
        elif value < current.value:
            current.left = self.__delete_wrapper2(current.left, value)
        elif value > current.value:
            current.right = self.__delete_wrapper2(current.right, value)

        else:  # value found
            if current.left is None:  # 1 or no children
                temp = current.right
                current = None  # delete node
                return temp  # return new root
            elif current.right is None:
                temp = current.left
                current = None
                return temp
            else:  # 2 children
                successor = self.__min_wrapper(current.right)
                current._value = successor  # copy value to node
                # get new root of subtree after deleting successor node
                current.right = self.__delete_wrapper2(current.right,
                                                       successor)

        return current

    def pre_order(self):
        """Print out values of the tree in pre-order traversal (root,L,R)."""
        return self.__pre_order_wrapper(self._root)

    def __pre_order_wrapper(self, current):
        """Private wrapper method for pre_order."""
        if current is None:
            return

        print(current.value, end=" ")
        self.__pre_order_wrapper(current.left)
        self.__pre_order_wrapper(current.right)

    def in_order(self):
        """Print out values of the tree in in-order traversal (L,root,R)."""
        return self.__in_order_wrapper(self._root)

    def __in_order_wrapper(self, current):
        """Private wrapper method for in_order."""
        if current is None:
            return

        self.__in_order_wrapper(current.left)
        print(current.value, end=" ")
        self.__in_order_wrapper(current.right)

    def post_order(self):
        """Print out values of the tree in post-order traversal (L,R,root)."""
        return self.__post_order_wrapper(self._root)

    def __post_order_wrapper(self, current):
        """Private wrapper method for post_order."""
        if current is None:
            return

        self.__post_order_wrapper(current.left)
        self.__post_order_wrapper(current.right)
        print(current.value, end=" ")

    def level_order(self):
        """Print out values of the tree in breadth-first order."""
        height = self.height()

        # explore down one level from root each iteration
        for idx in range(height):
            self.__print_level(self._root, idx + 1)

    def __print_level(self, current, level):
        """Private helper method for level_order."""
        if current is None:
            return
        elif level == 1:
            print(current.value, end=" ")
        elif level > 1:
            self.__print_level(current.left, level - 1)
            self.__print_level(current.right, level - 1)


TREE = RecursiveBST()
TREE.insert(4)
TREE.insert(5)
TREE.insert(2)
TREE.insert(3)

# pre should print out: 4 2 3 5
TREE.pre_order()
print('\n')
# in should print out: 2 3 4 5
TREE.in_order()
print('\n')
# post should print out: 3 2 5 4
TREE.post_order()
print('\n')
# level should print out 4 2 5 3
TREE.level_order()
print('\n')
