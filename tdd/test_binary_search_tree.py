import unittest
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
        self.assertEqual(len(bst), 0)

    def test_insert_single_node(self):
        bst = BinarySearchTree()
        bst.put(10, 'value10')
        self.assertIsNotNone(bst.root)
        self.assertEqual(bst.root.key, 10)
        self.assertEqual(bst.root.value, 'value10')
        self.assertEqual(len(bst), 1)

    def test_get_single_node(self):
        bst = BinarySearchTree()
        bst.put(10, 'value10')
        value = bst.get(10)
        self.assertEqual(value, 'value10')

    def test_insert_multiple_nodes(self):
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        self.assertEqual(len(bst), 3)
        self.assertEqual(bst.get(5), "value5")
        self.assertEqual(bst.get(3), "value3")

if __name__ == '__main__':
    unittest.main()