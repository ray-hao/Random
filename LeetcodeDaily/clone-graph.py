"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
            
        newNodes = {}
        done = set()
        todo = []
        todo.append(node)
        while len(todo) > 0:
            popped = todo.pop()
            if not popped:
                continue
            poppedVal = popped.val
            poppedNeighbors = popped.neighbors
            if poppedVal in done:
                continue
            else:
                done.add(poppedVal)
                if poppedVal not in newNodes:
                    addedNode = Node(poppedVal, [])
                    newNodes[poppedVal] = addedNode
                for neighbor in poppedNeighbors:
                    if neighbor.val not in newNodes:
                        addedNeighbor = Node(neighbor.val, [])
                        newNodes[neighbor.val] = addedNeighbor
                    if neighbor not in newNodes[poppedVal].neighbors:
                        newNodes[poppedVal].neighbors.append(newNodes[neighbor.val])
                    todo.append(neighbor)

        return newNodes[node.val]

