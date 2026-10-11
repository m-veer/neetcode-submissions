# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        if root:
            left = self.isValidBST(root.left)
            right = self.isValidBST(root.right)
            if left is None and right is None:
                return root
            if left is None:
                return root.val < right
            if right is None:
                return root.val > left
            if left is not None and right is not None:
                return root.val > left.val and root.val < right.val