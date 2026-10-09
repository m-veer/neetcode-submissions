# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return output
        queue = deque([root])
        while queue:
            length = len(queue)
            nodes = []
            for _ in range(length):
                node = deque.popleft(queue)
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(nodes[-1])
        return output