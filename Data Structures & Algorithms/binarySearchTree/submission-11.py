class Node:

    def __init__(self,key,val):
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
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = Node(key, val)
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = Node(key, val)
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return -1
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
        if not node:
            return None
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):    
        if not node:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._getMin(node.right)
                node.key, node.val = min_node.key, min_node.val
                node.right = self._remove(node.right, min_node.key)
                return node

    def getInorderKeys(self) -> List[int]:
        res = []
        self._inOrder(self.root, res)
        return res

    def _inOrder(self, node, res):
        if node:
            self._inOrder(node.left, res)
            res.append(node.key)
            self._inOrder(node.right, res)