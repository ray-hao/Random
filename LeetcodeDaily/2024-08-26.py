"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        vals = []
        self.helper(vals, root)
        return vals

    # Recursive
    def helper(self, vals, currentNode):
        if not currentNode:
            return
        if not currentNode.children:
            vals.append(currentNode.val)
            return

        for child in currentNode.children:
            self.helper(vals, child)
        vals.append(currentNode.val)
