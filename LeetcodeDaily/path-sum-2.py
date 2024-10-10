# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        retvals = []
        self.dfs(root, [], 0, targetSum, retvals)
        return retvals

    def dfs(self, current, currentPath, currentSum, targetSum, retvals):
        if not current.left and not current.right:
            if currentSum + current.val == targetSum:
                currentPath.append(current.val)
                retvals.append(tuple(currentPath))
                currentPath.pop()
            return

        if current.left:
            currentPath.append(current.val)
            self.dfs(current.left, currentPath, currentSum + current.val, targetSum, retvals)
            currentPath.pop()
        
        if current.right:
            currentPath.append(current.val)
            self.dfs(current.right, currentPath, currentSum + current.val, targetSum, retvals)
            currentPath.pop()
