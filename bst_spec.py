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
        node3 = bst.Node(3)
        node2 = bst.Node(2)
        node4 = bst.Node(4)

        tree = bst.BST()



if __name__ == '__main__':
    unittest.main()
