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
        current = self.findMin(self.root)
        return current.val if current else -1
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.remove_helper(self.root, key)

    def remove_helper(self, curr, key):
        if not curr:
            return None
        if key > curr.key:
            curr.right = self.remove_helper(curr.right, key)
        elif key < curr.key:
            curr.left = self.remove_helper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                min_node = self.findMin(curr.right)
                curr.key, curr.val = min_node.key, min_node.val
                curr.right = self.remove_helper(curr.right, min_node.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self._helper_inorder(self.root, res)
        return res
    
    def _helper_inorder(self, node, res):
        if node:
            self._helper_inorder(node.left, res)
            res.append(node.key)
            self._helper_inorder(node.right, res)
