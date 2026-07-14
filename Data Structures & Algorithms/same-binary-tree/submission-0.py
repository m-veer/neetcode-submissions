# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not (node1 and node2):
                return False

            traverse(node1.left, node2.left)

            if node1.val != node2.val:
                return False

            traverse(node1.right, node2.right)

            return True

        return traverse(p, q) and traverse(p.left, q.left) and traverse(p.right, q.right)