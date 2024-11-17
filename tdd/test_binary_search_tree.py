import unittest
from binary_search_tree import BinarySearchTree

class TestBInarySearchTree(unittest.TestCase):
    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.root)
        self.assertEqual(len(bst), 0)


if __name__ == '__main__':
    unittest.main()