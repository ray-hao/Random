# had to use hint: dfs from each leaf node.
# how do we dfs efficiently from each leaf node?
# can we use inorder traversal array to dfs from each leaf node?


class PTreeNode:

    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leafNodes = []
        proot = self.dfs(root, leafNodes)
        total = 0
        for leaf in leafNodes:
            total += self.leafDfs(leaf, leaf, distance, leafNodes, [])
        
        return int(total / 2)

    def dfs(self, root, leafNodes):
        if root == None:
            return
        
        newNode = PTreeNode(root.val)
        leftNode = None
        rightNode = None
        if root.left:
            leftNode = self.dfs(root.left, leafNodes)
        if root.right:
            rightNode = self.dfs(root.right, leafNodes)
        if leftNode:
            newNode.left = leftNode
            leftNode.parent = newNode
        if rightNode:
            newNode.right = rightNode
            rightNode.parent = newNode

        if newNode.left == None and newNode.right == None:
            leafNodes.append(newNode)

        return newNode
        
    def leafDfs(self, current, startingNode, stepsLeft, leafNodes, seen):
        if stepsLeft < 0:
            return 0
        if current in seen:
            return 0

        seen.append(current)

        if current in leafNodes and current != startingNode:
            return 1
        
        parentCount = 0
        leftCount = 0
        rightCount = 0
        if current.parent:
            parentCount = self.leafDfs(current.parent, startingNode, stepsLeft - 1, leafNodes, seen)
        if current.left:
            leftCount = self.leafDfs(current.left, startingNode, stepsLeft - 1, leafNodes, seen)
        if current.right:
            rightCount = self.leafDfs(current.right, startingNode, stepsLeft - 1, leafNodes, seen)
        
        return parentCount + leftCount + rightCount
