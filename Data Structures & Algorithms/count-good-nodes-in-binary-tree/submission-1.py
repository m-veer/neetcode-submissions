# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(root, max_path):
            if root:
                if root.val >= max_path:
                    self.count += 1
                    max_path = root.val
                traverse(root.left, max_path)
                traverse(root.right, max_path)
        traverse(root, root.val)
        return self.count