# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inverted_tree = None
        if root:
            if not inverted_tree:
                inverted_tree = TreeNode(root.val, root.right, root.left)
            inverted_tree.right = self.invertTree(root.left)
            inverted_tree.left = self.invertTree(root.right)
        return inverted_tree