# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def traverse(root):
            if not root:
                return 0
            if root.left is None and root.right is None:
                return root.val
            # if root.val < 0:
            #     return 0
            left = traverse(root.left)
            right = traverse(root.right)
            self.max = max(self.max, root.val + left + right) # Path Sum
            return max(root.val + left, root.val + right) # Best of the 2 child nodes
        traverse(root)
        return self.max