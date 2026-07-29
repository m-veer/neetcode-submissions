# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.output = False
        def isSameSubTree(first_tree, second_tree):
            if first_tree == None and second_tree == None:
                return True
            if first_tree != None and second_tree != None:
                return first_tree.val == second_tree.val and isSameSubTree(first_tree.left, second_tree.left) and isSameSubTree(first_tree.right, second_tree.right)
                # return first_tree.val == second_tree.val and isSameSubTree(first_tree.left, second_tree.left) and isSameSubTree(first_tree.right, second_tree.right)
            return False

        def traverse(r, sR):
            if r and sR:
                if r.val == sR.val and sR.left == None and sR.right == None:
                    return True
                elif r.val == sR.val:
                    self.output = isSameSubTree(r, sR)
                    return self.output
                traverse(r.left, sR)
                traverse(r.right, sR)
            return self.output
        return traverse(root, subRoot)