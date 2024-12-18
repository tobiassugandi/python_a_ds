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
        self.assertEqual(bst.get_node(10), bst.get_node(5).parent)

    def test_get_nonexistent_key(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.get(20))
        bst.put(10, "value10")
        self.assertIsNone(bst.get(20))

    def test_contains_method(self):
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        self.assertTrue(10 in bst)
        self.assertTrue(5 in bst)
        self.assertTrue(3 in bst)

    def test_delete_leaf(self):
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.delete(5)
        self.assertIsNone(bst.root.left_child)
        self.assertEqual(len(bst), 1)
        self.assertFalse(5 in bst)
        self.assertTrue(10 in bst)
        bst.delete(10)
        self.assertIsNone(bst.root)
        self.assertFalse(10 in bst)


    def test_delete_node_w_one_child(self):
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        # delete a non-root node with a child
        bst.delete(5)
        self.assertIsNone(bst.get_node(5))
        self.assertEqual(len(bst), 2)
        self.assertTrue(10 in bst and 3 in bst)
        self.assertTrue(bst.get_node(10) == bst.get_node(3).parent)
        # delete a root node with a child
        bst.delete(10)
        self.assertEqual(bst.get_node(3), bst.root)

    def test_delete_node_w_two_child(self):
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        bst.put(7, "value7")
        bst.delete(5)
        self.assertEqual(bst.get_node(10).left_child, bst.get_node(7))
        self.assertEqual(bst.get_node(3).parent, bst.get_node(7))
        self.assertEqual(bst.get_node(7).parent, bst.get_node(10))
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        bst.put(7, "value7")
        bst.put(6, "value6")
        bst.delete(5)
        self.assertEqual(bst.get_node(10).left_child, bst.get_node(6))
        self.assertEqual(bst.get_node(3).parent, bst.get_node(6))
        self.assertEqual(bst.get_node(6).parent, bst.get_node(10))
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(3, "value3")
        bst.put(6, "value6")
        bst.put(7, "value7")
        bst.delete(5)
        self.assertEqual(bst.get_node(10).left_child, bst.get_node(6))
        self.assertEqual(bst.get_node(3).parent, bst.get_node(6))
        self.assertEqual(bst.get_node(6).parent, bst.get_node(10))
        bst = BinarySearchTree()
        bst.put(10, "value10")
        bst.put(5, "value5")
        bst.put(12, "value12")
        bst.delete(10)
        self.assertEqual(bst.root.key,  12)

    def test_in_order_traversal(self):
        bst = BinarySearchTree()
        for key in [10, 5, 13, 4, 2]:
            bst.put(key, f"value{key}")
        traversal = [key for key in bst]
        self.assertEqual(traversal, [2,4,5,10,13])

if __name__ == '__main__':
    unittest.main()