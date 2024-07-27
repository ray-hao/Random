import heapq
#
# ok basically for each character we want to transform it from the source character to a target character
# and transitioning between characters each has a weight
#
# we can just model this problem as a directed graph problem, and apply dijkstra and memoize source to target costs 
# to avoid recomputation in the future.
#


class GraphNode:
    def __init__(self, value = 0, neighbors = []):
        self.value = value
        self.neighbors = neighbors

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        nodeList = set()
        for char in original:
            nodeList.add(char)
        for char in changed:
            nodeList.add(char)

        graphNodes = {}
        for char in nodeList:
            newNode = GraphNode(char, [])
            graphNodes[char] = newNode

        length = len(original)
        for i in range(length):
            originNode = original[i]
            destNode = changed[i]
            transitionCost = cost[i]

            graphNodes[originNode].neighbors.append((destNode, transitionCost))

        wordLength = len(source)
        runningCost = 0
        memo = {}
        for pos in range(wordLength):
            if source[pos] in memo:
                if source[pos] not in list(memo[source[pos]].keys()) or (memo[source[pos]])[target[pos]] == float('inf'):
                    return -1
                else:
                    runningCost += (memo[source[pos]])[target[pos]]
                    continue
            newCost = self.dijkstra(graphNodes, source[pos], target[pos], memo)
            if newCost == -1:
                return -1
            else:
                runningCost += newCost

        return runningCost

    def dijkstra(self, graph, source, target, memo):
        if source == target:
            return 0

        if source not in list(graph.keys()):
            return -1

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, source))
        distances = {}

        for key in list(graph.keys()):
            if key == source:
                distances[key] = 0
            else:
                distances[key] = float('inf')

        while (len(heap) > 0):
            popped = heapq.heappop(heap)
            currentCost = popped[0]
            currentNode = popped[1]

            for neighbor in graph[currentNode].neighbors:
                neighborNode = neighbor[0]
                neighborCost = neighbor[1]
                if currentCost + neighborCost < distances[neighborNode]:
                    distances[neighborNode] = currentCost + neighborCost
                    heapq.heappush(heap, (currentCost + neighborCost, neighborNode))
        
        if target not in distances or distances[target] == float('inf'):
            return -1
        
        memo[source] = distances

        return distances[target] 
