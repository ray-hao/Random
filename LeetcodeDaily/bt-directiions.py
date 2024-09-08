#
# we know that if one node is a child of another, it's easy through dfs
# otherwise, we'll need to find the LCA, and paths from source to LCA, then LCA to dest
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        LCA = self.helper(root, startValue, destValue)
    
        # LCA to source
        pathToSource = self.dfs(LCA, startValue, [])

        # LCA to desc
        pathToDest = self.dfs(LCA, destValue, [])

        print(pathToSource, pathToDest)

        return "U" * len(pathToSource) + "".join(pathToDest)
        
    def helper(self, current, node1, node2):
        if not current:
            return False
        if current.val == node1 or current.val == node2:
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

    # find path between ancestor and child, returning path
    def dfs(self, current, target, path):
        if not current:
            return None
        if current.val == target:
            return path
        else:
            path.append("L")
            left = self.dfs(current.left, target, path)
            if left:
                return left
            path.pop()
            path.append("R")
            right = self.dfs(current.right, target, path)
            if right:
                return right
            path.pop()
            


        
