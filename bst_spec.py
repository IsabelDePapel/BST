import unittest
import bst


class TestNodeClass(unittest.TestCase):
    """Test basic node class functionality."""

    def setUp(self):
        self.node = bst.Node(3)

    def test_value(self):
        self.assertEqual(self.node.value, 3)

    def test_default_left(self):
        self.assertIsNone(self.node.left)

    def test_set_left(self):
        left_val = 2
        new_node = bst.Node(left_val)
        self.node.left = new_node
        self.assertEqual(self.node.left, new_node)

    def test_default_right(self):
        self.assertIsNone(self.node.right)

    def test_set_right(self):
        right_val = 4
        new_node = bst.Node(right_val)
        self.node.right = new_node
        self.assertEqual(self.node.right, new_node)


class TestBSTClass(unittest.TestCase):
    """Test basic BST class functionality."""

    def setUp(self):
        self.empty_tree = bst.BST()

        self.small_tree = bst.BST()
        self.small_tree.insert(4)

        self.medium_tree = bst.BST()
        self.medium_tree.insert(4)
        self.medium_tree.insert(3)
        self.medium_tree.insert(5)

        self.large_tree = bst.BST()
        self.large_tree.insert(4)
        self.large_tree.insert(5)
        self.large_tree.insert(6)
        self.large_tree.insert(2)
        self.large_tree.insert(3)
        self.large_tree.insert(0)
        self.large_tree.insert(1)
        self.large_tree.insert(3)

    def test_search(self):
        self.assertFalse(self.empty_tree.search(3))

        self.assertFalse(self.small_tree.search(3))
        self.assertTrue(self.small_tree.search(4))

        self.assertTrue(self.medium_tree.search(5))
        self.assertFalse(self.medium_tree.search(-5))

    def test_height(self):
        self.assertEqual(self.empty_tree.height(), 0)
        self.assertEqual(self.small_tree.height(), 1)
        self.assertEqual(self.medium_tree.height(), 2)

        self.medium_tree.insert(2)
        self.assertEqual(self.medium_tree.height(), 3)

        self.assertEqual(self.large_tree.height(), 4)

    

if __name__ == '__main__':
    unittest.main()
