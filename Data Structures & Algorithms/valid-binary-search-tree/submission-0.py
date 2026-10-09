# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.isValid = True

        def traverse(root):
            if root:
                traverse(root.left)
                self.prev = root if not self.prev else self.prev
                if root.val < self.prev.val:
                    self.isValid = False
                self.prev = root
                traverse(root.right)
        traverse(root)
        return self.isValid