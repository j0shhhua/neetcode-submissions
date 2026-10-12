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
        curr = root
        if key < curr.val:
            curr.left = self.deleteNode(root.left, key)
        elif key > curr.val:
            curr.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = curr.right
                while minNode and minNode.left:
                    minNode = minNode.left
                curr.val = minNode.val
                curr.right = self.deleteNode(curr.right, minNode.val)
        return root