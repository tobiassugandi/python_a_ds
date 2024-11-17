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





if __name__ == '__main__':
    unittest.main()