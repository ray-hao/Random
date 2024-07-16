# We can't arbitrarily build the tree, since we don't have access to all nodes on first pass.
# Let's make one pass where we just make and store all nodes based on value, with a dict for quick access
# and then build the actual tree in the second pass. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = []
        positions = {}
        for desc in descriptions:
            currNode = TreeNode(desc[1])
            nodes.append(currNode)
            positions[desc[1]] = len(nodes) - 1
        
        rootNode = None
        for description in descriptions:

            currNode = nodes[positions[description[1]]]
            if description[0] not in positions:
                newNode = TreeNode(description[0])
                rootNode = newNode
                nodes.append(newNode)
                positions[newNode.val] = len(nodes) - 1

            parentNode = nodes[positions[description[0]]]
            isLeft = description[2]
            
            if isLeft:
                parentNode.left = currNode
            else:
                parentNode.right = currNode
        
        return rootNode
