# We know the path has to go through the lowest common ancestor, since the path between 
# 2 nodes in a tree is unique. Let's find the LCA first, then find paths from LCA to
# startValue and EndValue using dfs or anything else.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        LCA = self.lowestCommonAncestor(root, startValue, destValue)
        startDirections = self.dfs(LCA, startValue, [])
        endDirections = self.dfs(LCA, destValue, [])
        endtoLCADirections = "".join(endDirections)
        
        # just make all left or right steps UP
        startToLCADirections = "U" * len(startDirections)

        return startToLCADirections + endtoLCADirections

    # Find the LCA, using dfs - if we've reached a node where the node's value is a target,
    # we should return it. If it itself is the LCA, we're fine. If the other target node is 
    # in a different branch splitting higher up, we'll have 2 return values at that node, so 
    # we know where it split (LCA).
    def lowestCommonAncestor(self, root, node1, node2):
        if root.val == node1 or root.val == node2:
            return root
        
        leftSol = None
        rightSol = None
        if (root.left):
            leftSol = self.lowestCommonAncestor(root.left, node1, node2)
        if (root.right):
            rightSol = self.lowestCommonAncestor(root.right, node1, node2)

        if leftSol and rightSol:
            return root
        if leftSol:
            return leftSol
        if rightSol:
            return rightSol
        return None

    # To save memory, avoid duplicating strings, so directions should be an array
    def dfs(self, root, targetValue, directions):
        if root.val == targetValue:
            return directions
        if not root.val:
            return False

        directions.append("L")
        if root.left:
            leftSol = self.dfs(root.left, targetValue, directions)
            if leftSol:
                return leftSol

        directions.pop()
        directions.append("R")

        if root.right:
            rightSol = self.dfs(root.right, targetValue, directions)
            if rightSol:
                return rightSol

        directions.pop()
        return False
