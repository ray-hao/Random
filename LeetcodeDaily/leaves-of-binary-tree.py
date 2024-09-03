#
# Basically we want to keep track of how far from a leaf each node is.
# We can do this using some postorder traversal
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelMap = defaultdict(lambda: [])
        self.helper(root, levelMap)
        retval = []
        current = 1
        levelMapKeys = levelMap.keys()
        while (current in levelMapKeys):
            retval.append(levelMap[current])
            current += 1
        return retval

    def helper(self, current: TreeNode, levelList: defaultdict[int, List[int]]) -> int:
        if not current:
            return 0
        if not current.left and not current.right:
            retval = 1
            levelList[retval].append(current.val)
            return retval
        
        else:
            retval = 1 + max(self.helper(current.left, levelList), self.helper(current.right, levelList))
            levelList[retval].append(current.val)
            return retval
