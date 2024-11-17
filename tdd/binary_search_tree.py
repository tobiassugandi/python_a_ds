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

    def has_two_children(self):
        return self.left_child is not None and self.right_child is not None

    def has_one_child(self):
        return not self.is_leaf() and not self.has_two_children()


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
                    if node.right_child:
                        node.parent.right_child = node.right_child
                        node.right_child.parent = node.parent
                    else: # node has left child
                        node.parent.right_child = node.left_child
                        node.left_child.parent = node.parent
                elif node.is_left_child():
                    if node.right_child:
                        node.parent.left_child = node.right_child
                        node.right_child.parent = node.parent
                    else: # node has left child
                        node.parent.left_child = node.left_child
                        node.left_child.parent = node.parent
                else: # root node w one child
                    self.root = node.right_child if node.right_child else node.left_child
            else: # node has 2 children
                # find successor
                successor = node.right_child
                while successor.left_child:
                    successor = successor.left_child
                # remove parent-successor and successor-child relation, this successor must either be a leaf or only has 1 child
                self.delete(successor.key)

                # back to deleting current node
                # rearrange relation to parent
                if node.is_left_child():
                    node.parent.left_child = successor
                if node.is_right_child():
                    node.parent.right_child = successor
                successor.parent = node.parent
                # rearrange relation with right and left children
                successor.left_child = node.left_child
                node.left_child.parent = successor
                if node.right_child:
                    successor.right_child = node.right_child
                    node.right_child.parent = successor
                else:
                    successor.right_child = None
            self.size -= 1
        else: # nothing to delete
            print(f"key {key} not found, cannot be deleted")
            pass
