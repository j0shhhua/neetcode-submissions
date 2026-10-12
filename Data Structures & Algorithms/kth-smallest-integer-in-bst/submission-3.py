# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inOrder(root)
        return self.res[k - 1]
    
    def inOrder(self, root):
        if root is None:
            return []
        self.inOrder(root.left)
        self.res.append(root.val)
        self.inOrder(root.right)
        