class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        edgeMap = defaultdict(lambda : [])
        for i in range(len(edges)):
            [v1, v2] = edges[i]
            succ = succProb[i]
            edgeMap[v1].append([v2, succ])
            edgeMap[v2].append([v1, succ])

        greatest = [0] * n
        greatest[start_node] = 1

        maxHeap = []
        heapq.heapify(maxHeap)
        for edge in edgeMap[start_node]:
            [adj, succ] = edge
            if succ > greatest[adj]:
                heapq.heappush(maxHeap, (-1 * succ, adj))
                greatest[adj] = succ

        while len(maxHeap) > 0:
            (succ, vertex) = heapq.heappop(maxHeap)
            succ = succ * -1
            for edge in edgeMap[vertex]:
                [adjacent, prob] = edge
                if succ * prob > greatest[adjacent]:
                    heapq.heappush(maxHeap, (-1 * succ * prob, adjacent))
                    greatest[adjacent] = succ * prob

        return greatest[end_node]
