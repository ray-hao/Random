# ok first we should probably define a class to we can actually build the graph.
# for each query, we want to find the path between the start and end node.
# we can do that with bfs. during this bfs we can also find the path from the start
# node to the adjacent node, and we can determine which node is closest along the path
# by comparing the prefixes of the paths. 

class Node:

    def __init__(self, val = 0, adjacentNodes = []):
        self.val = val
        self.adjacentNodes = adjacentNodes

    def __str__(self):
        return "Node value: " + str(self.val) + ", Neighbors: " + ", ".join(str(adj.val) for adj in self.adjacentNodes)

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graphNodes = []
        for i in range(n):
            newNode = Node(i, [])
            graphNodes.append(newNode)
        
        for edge in edges:
            graphNodes[edge[0]].adjacentNodes.append(graphNodes[edge[1]])
            graphNodes[edge[1]].adjacentNodes.append(graphNodes[edge[0]])
        
        answers = []
        for q in query:
            path1 = []
            path2 = []
            seen = set()
            self.bfs(graphNodes[q[0]], graphNodes[q[1]], path1, [], seen)
            seen.clear()
            self.bfs(graphNodes[q[0]], graphNodes[q[2]], path2, [], seen)
            lastSame = 0
            path1 = path1[0]
            path2 = path2[0]
            while lastSame < len(path1) and lastSame < len(path2):
                if path1[lastSame] == path2[lastSame]:
                    lastSame += 1
                else:
                    break

            answers.append(int(path1[lastSame - 1]))
        return answers
            

    def bfs(self, root, target, path, currentPath, seen):
        if root in seen:
            return
        seen.add(root)

        if root == target:
            path.append(currentPath + [root.val])
            return
        
        for neighbor in root.adjacentNodes:
            self.bfs(neighbor, target, path, currentPath + [root.val], seen)
        
