# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                min_node = self.minCur(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root

    def minCur(self, node):
        curr = node
        while curr and curr.left != None:
            curr = curr.left
        return curr
        