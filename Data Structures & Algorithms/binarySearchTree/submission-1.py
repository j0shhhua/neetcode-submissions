class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        self.root = self._insert(self.root, key, val)

    def _insert(self, node, key, val):
        if not node:
            return TreeNode(key, val)
        if key < node.key:
            node.left = self._insert(node.left, key, val)
        elif key > node.key:
            node.right = self._insert(node.right, key, val)
        else:
            node.val = val  # duplicate key: override value
        return node

    def get(self, key):
        node = self._get(self.root, key)
        return node.val if node else -1

    def _get(self, node, key):
        if not node:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        return node

    def getMin(self):
        if not self.root:
            return -1
        node = self.root
        while node.left:
            node = node.left
        return node.val

    def getMax(self):
        if not self.root:
            return -1
        node = self.root
        while node.right:
            node = node.right
        return node.val

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Two children: replace with inorder successor (min of right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key, node.val = successor.key, successor.val
            node.right = self._remove(node.right, successor.key)
        return node

    def getInorderKeys(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)