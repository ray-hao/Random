import heapq

class GraphNode:
    def __init__(self, value = 0, neighbors = []):
        self.value = value
        self.neighbors = neighbors

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graphNodes = []
        
        for i in range(n):
            newNode = GraphNode(i, [])
            graphNodes.append(newNode)
        
        for highway in highways:
            graphNodes[highway[0]].neighbors.append((highway[1], highway[2]))
            graphNodes[highway[1]].neighbors.append((highway[0], highway[2]))

        dpArray = [[float('inf')] * n for i in range(discounts + 1)]
        
        for i in range(discounts + 1):
            dpArray[i][0] = 0
        
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, discounts))

        while (len(heap) > 0):
            popped = heapq.heappop(heap)
            currentNode = popped[0]
            currentDistance = popped[1]
            discountsLeft = popped[2]

            for neighbor in graphNodes[currentNode].neighbors:
                if (discountsLeft > 0):
                    if currentDistance + int(neighbor[1] / 2) < dpArray[discountsLeft - 1][neighbor[0]]:
                        dpArray[discountsLeft - 1][neighbor[0]] = currentDistance + int(neighbor[1] / 2)
                        heapq.heappush(heap, (neighbor[0], currentDistance + int(neighbor[1] / 2), discountsLeft - 1))
                if currentDistance + neighbor[1] < dpArray[discountsLeft][neighbor[0]]:
                    dpArray[discountsLeft][neighbor[0]] = currentDistance + neighbor[1]
                    heapq.heappush(heap, (neighbor[0], currentDistance + neighbor[1], discountsLeft))
        
        minVal = float('inf')

        for row in dpArray:
            minVal = min(minVal, row[-1])

        if minVal == float('inf'):
            return -1

        return minVal
