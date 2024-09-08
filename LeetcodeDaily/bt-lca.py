# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
        
    def helper(self, current, node1, node2):
        if not current:
            return False
        if current.val == node1.val or current.val == node2.val:
            return current
        else:
            leftSol = self.helper(current.left, node1, node2)
            rightSol = self.helper(current.right, node1, node2)
            if leftSol and rightSol:
                return current
            elif leftSol and not rightSol:
                return leftSol
            else:
                return rightSol
  
