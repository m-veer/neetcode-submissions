# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        self.is_valid = True
        def checkValidBST(root, low, high):
            if not self.is_valid or not root:
                return
            if low is not None:
                self.is_valid = root.val > low
            if high is not None:
                self.is_valid = root.val < high
            if root.left is None and root.right is None:
                return
            checkValidBST(root.left, low, root.val)
            checkValidBST(root.right, root.val ,high)
        checkValidBST(root, None, None)
        return self.is_valid