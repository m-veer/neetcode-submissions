# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if (not node1 and node2) or (node1 and not node2):
                return False

            if not node1 and not node2:
                return True

            if (not node1.left and node2.left) or (node1.left and not node2.left):
                return False
            traverse(node1.left, node2.left)

            if node1.val != node2.val:
                return False

            if (not node1.right and node2.right) or (node1.right and not node2.right):
                return False
            traverse(node1.right, node2.right)

            return True

        return traverse(p, q) and traverse(p.left, q.left) and traverse(p.right, q.right) if p or q else True