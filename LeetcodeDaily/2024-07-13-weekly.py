# probably relates to finding the LCA. 
# we can probably just find LCA and then dfs from lca to get distances


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        lca = self.getLCA(root, p, q)
        myDict = {}
        self.dfs(lca, 0, myDict)
        return myDict[p] + myDict[q]

    def getLCA(self, root, p, q):
        if root == None:
            return None
        
        if root.val == p or root.val == q:
            return root
        
        left = self.getLCA(root.left, p, q)
        right = self.getLCA(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right

    def dfs(self, root, distance, discovered):
        if not root:
            return
        
        discovered[root.val] = distance
        self.dfs(root.left, distance + 1, discovered)
        self.dfs(root.right, distance + 1, discovered)        
