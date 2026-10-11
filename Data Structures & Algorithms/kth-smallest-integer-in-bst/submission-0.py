# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.output = None
        def traverse(root):
            if root and self.output is None:
                traverse(root.left)
                self.k -= 1
                if self.k == 0:
                    self.output = root.val
                traverse(root.right)
        traverse(root)
        return self.output