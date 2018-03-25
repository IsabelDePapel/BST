import unittest
import node
import bst_recur as rbst
import bst_iter as ibst


class TestNodeClass(unittest.TestCase):
    """Test basic node class functionality."""

    def setUp(self):
        self.node = node.Node(3)

    def test_value(self):
        self.assertEqual(self.node.value, 3)

    def test_default_left(self):
        self.assertIsNone(self.node.left)

    def test_set_left(self):
        left_val = 2
        new_node = node.Node(left_val)
        self.node.left = new_node
        self.assertEqual(self.node.left, new_node)

    def test_default_right(self):
        self.assertIsNone(self.node.right)

    def test_set_right(self):
        right_val = 4
        new_node = node.Node(right_val)
        self.node.right = new_node
        self.assertEqual(self.node.right, new_node)


class TestRecursiveBSTClass(unittest.TestCase):
    """Test basic BST class functionality."""

    def setUp(self):
        self.empty_tree = rbst.RecursiveBST()

        self.small_tree = rbst.RecursiveBST()
        self.small_tree.insert(4)

        self.medium_tree = rbst.RecursiveBST()
        self.medium_tree.insert(4)
        self.medium_tree.insert(3)
        self.medium_tree.insert(5)

        self.large_tree = rbst.RecursiveBST()
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

    def test_min(self):
        self.assertIsNone(self.empty_tree.min())
        self.assertEqual(self.small_tree.min(), 4)
        self.assertEqual(self.medium_tree.min(), 3)

    def test_delete_root(self):
        with self.assertRaises(IndexError):
            self.empty_tree.delete(4)

        self.assertTrue(self.small_tree.search(4))
        self.small_tree.delete(4)
        self.assertFalse(self.small_tree.search(4))

        self.assertTrue(self.medium_tree.search(4))
        self.medium_tree.delete(4)
        self.assertFalse(self.medium_tree.search(4))
        self.assertEqual(self.medium_tree._root.value, 5)

    def test_delete_leaf(self):
        self.assertTrue(self.large_tree.search(6))
        self.large_tree.delete(6)
        self.assertFalse(self.large_tree.search(6))

    def test_delete_node_with_one_child(self):
        self.assertTrue(self.large_tree.search(1))
        self.large_tree.delete(1)
        self.assertFalse(self.large_tree.search(1))

    def test_delete_node_with_two_children(self):
        self.assertTrue(self.large_tree.search(2))
        self.large_tree.delete(2)
        self.assertFalse(self.large_tree.search(2))

        self.large_tree.in_order()

    def test_delete2_root(self):
        self.assertIsNone(self.empty_tree.delete2(2))

        self.assertTrue(self.small_tree.search(4))
        self.assertIsNone(self.small_tree.delete(4))
        self.assertFalse(self.small_tree.search(4))

        self.assertTrue(self.medium_tree.search(4))
        self.assertEqual(self.medium_tree.delete2(4).value, 5)
        self.assertEqual(self.medium_tree._root.value, 5)
        self.assertFalse(self.medium_tree.search(4))

    def test_delete2_leaf(self):
        self.assertTrue(self.large_tree.search(6))
        self.assertEqual(self.large_tree.delete2(6).value, 4)
        self.assertFalse(self.large_tree.search(6))

    def test_delete2_with_one_child(self):
        self.assertTrue(self.large_tree.search(1))
        self.assertEqual(self.large_tree.delete2(1).value, 4)
        self.assertFalse(self.large_tree.search(1))

    def test_delete2_node_with_two_children(self):
        self.assertTrue(self.large_tree.search(2))
        self.assertEqual(self.large_tree.delete2(2).value, 4)
        self.assertFalse(self.large_tree.search(2))

        self.large_tree.in_order()


class TestIterativeBSTClass(unittest.TestCase):
    """Test functionality of iterative BST."""
    def setUp(self):
        self.empty_tree = ibst.IterativeBST()

        self.small_tree = ibst.IterativeBST()
        self.small_tree.insert(4)

        self.medium_tree = ibst.IterativeBST()
        self.medium_tree.insert(4)
        self.medium_tree.insert(3)
        self.medium_tree.insert(5)

        self.large_tree = ibst.IterativeBST()
        self.large_tree.insert(4)
        self.large_tree.insert(5)
        self.large_tree.insert(6)
        self.large_tree.insert(2)
        self.large_tree.insert(3)
        self.large_tree.insert(0)
        self.large_tree.insert(1)
        self.large_tree.insert(3)

    def test_search(self):
        self.assertFalse(self.empty_tree.search(2))
        self.assertTrue(self.small_tree.search(4))


if __name__ == '__main__':
    unittest.main()
