class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def is_left_child(self):
        return self.parent and self == self.parent.left_child

    def is_right_child(self):
        return self.parent and self == self.parent.right_child

    def has_one_child(self):
        return self.left_child or self.right_child



class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent = current_node)
        else:
            if current_node.right_child:
               self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent = current_node)

    def get(self, key):
        node = self._get_node(key, self.root)
        if node:
            return node.value
        else:
            return None

    def get_node(self, key):
        return self._get_node(key, self.root)

    def _get_node(self, key, current_node):
        if not current_node:
            print(f"key {key} not found")
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get_node(key, current_node.left_child)
        else:
            return self._get_node(key, current_node.right_child)

    def __contains__(self, key):
        return self.get(key) is not None

    def delete(self, key):
        node = self._get_node(key, self.root)
        if node:
            if node.is_leaf():
                if node.is_left_child():
                    node.parent.left_child = None
                elif node.is_right_child():
                    node.parent.right_child = None
                else: # leaf node w/o parent ==> root
                    self.root = None
            elif node.has_one_child():
                if node.is_right_child():
                    pass
                else:
                    pass
            self.size -= 1
        else: # nothing to delete
            print(f"key {key} not found, cannot be deleted")
            pass
