# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = None

        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if self.max is not None:
                self.max = max(self.max, root.val + left + right) # Path Sum
            else:
                self.max = root.val
            return max(root.val + left, root.val + right) # Best of the 2 child nodes
        traverse(root)
        return self.max