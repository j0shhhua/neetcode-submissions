# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.itr = 0

        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            self.arr.append(curr.val)
            curr = curr.right

    def next(self) -> int:
        val = self.arr[self.itr]
        self.itr += 1
        return val

    def hasNext(self) -> bool:
        return self.itr < len(self.arr)