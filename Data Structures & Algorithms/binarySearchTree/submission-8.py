class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key, val)
            return
        new = Node(key, val)
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        res = self._getMin(self.root)
        return res.val if res else -1

    def _getMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if not self.root:
            return -1
        res = self.root
        while res.right:
            res = res.right
        return res.val

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return None
        curr = node
        if key < curr.key:
            curr.left = self._remove(curr.left, key)
        elif key > curr.key:
            curr.right = self._remove(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                min_node = self._getMin(curr.right)
                curr.key, curr.val = min_node.key, min_node.val
                curr.right = self._remove(curr.right, min_node.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self._inOrder(self.root, res)
        return res

    def _inOrder(self, node, res):
        if node:
            self._inOrder(node.left, res)
            res.append(node.key)
            self._inOrder(node.right, res)    
