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
        output.append(queue[-1].val)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = deque.popleft(queue)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                output.append(queue[-1].val)
        return output