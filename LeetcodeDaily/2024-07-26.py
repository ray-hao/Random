import heapq

class GraphNode:
    def __init__(self, value = 0, neighbors = []):
        self.value = value
        self.neighbors = neighbors

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graphNodes = []
        for i in range(n):
            newNode = GraphNode(i, [])
            graphNodes.append(newNode)
        
        for edge in edges:
            graphNodes[edge[0]].neighbors.append((edge[1], edge[2]))
            graphNodes[edge[1]].neighbors.append((edge[0], edge[2]))

        fewest = float('inf')
        amounts = []
        for i in range(n):
            retval = self.dijkstra(i, graphNodes, distanceThreshold)
            fewest = min(fewest, retval)
            amounts.append(retval)

        for i in range(n - 1, -1, -1):
            if amounts[i] == fewest:
                return i
        
    def dijkstra(self, start, graphNodes, maxDistance):
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, start))
        distances = [float('inf')] * len(graphNodes)
        distances[start] = 0

        while (len(heap) > 0):
            popped = heapq.heappop(heap)
            currentDistance = popped[0]
            currentNode = popped[1]

            if currentDistance > maxDistance: break

            for [neighborNode, neighborDistance] in graphNodes[currentNode].neighbors:
                if currentDistance + neighborDistance < distances[neighborNode]:
                    heapq.heappush(heap, (currentDistance + neighborDistance, neighborNode))
                    distances[neighborNode] = currentDistance + neighborDistance

        count = 0
        for dist in distances:
            if dist != float('inf') and dist <= maxDistance:
                count += 1

        return count
