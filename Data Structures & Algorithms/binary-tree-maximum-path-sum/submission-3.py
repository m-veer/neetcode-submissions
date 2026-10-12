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
            
            root_value = root.val
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            if root.val < 0:
                root_value = 0
            return max(root_value + left, root_value + right) # Best of the 2 child nodes
        traverse(root)
        return self.max