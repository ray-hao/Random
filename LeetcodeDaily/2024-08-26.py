"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    #
    # Iterative
    #

    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []

        postOrder = []
        stack = []
        seen = set()
        stack.append(root)
        while len(stack) > 0:
            popped = stack.pop()
            unvisitedChild = False
            for child in popped.children:
                if child not in seen:
                    stack.append(popped)
                    stack.append(child)
                    unvisitedChild = True
                    break
            
            if unvisitedChild:
                continue
            
            postOrder.append(popped.val)
            seen.add(popped)

        return postOrder
    #
    # Recursive
    #
    
    # def postorder(self, root: 'Node') -> List[int]:
    #     vals = []
    #     self.helper(vals, root)
    #     return vals

    # def helper(self, vals, currentNode):
    #     if not currentNode:
    #         return
    #     if not currentNode.children:
    #         vals.append(currentNode.val)
    #         return

    #     for child in currentNode.children:
    #         self.helper(vals, child)
    #     vals.append(currentNode.val)
