# 
# basically, we want a path from (0, 0) to (n-1, n-1)
# and the time t will be the greatest value along that path.
#
# can we do a dfs with dijkstra?
# Prim's algorithm
#

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        seen = {}
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (grid[0][0], (0, 0)))
        n = len(grid)
        
        while len(minHeap) != 0:
            current = heapq.heappop(minHeap)
            (currentTime, (y, x)) = current
            seen[(y, x)] = currentTime
            if (y, x) == (n-1, n-1):
                return currentTime
            # left
            if (x > 0):
                if (y, x-1) not in seen:
                    seen[y, x - 1] = max(currentTime, grid[y][x - 1])
                    heapq.heappush(minHeap, (max(currentTime, grid[y][x - 1]), (y, x - 1)))
            # right
            if (x < n-1):
                if (y, x+1) not in seen:
                    seen[y, x + 1] = max(currentTime, grid[y][x + 1])
                    heapq.heappush(minHeap, (max(currentTime, grid[y][x + 1]), (y, x + 1)))
            # down
            if (y < n -1):
                if (y + 1, x) not in seen:
                    seen[y + 1, x] = max(currentTime, grid[y + 1][x])
                    heapq.heappush(minHeap, (max(currentTime, grid[y + 1][x]), (y + 1, x)))
            # down
            if (y > 0):
                if (y - 1, x) not in seen:
                    seen[y -1, x] = max(currentTime, grid[y -1][x])
                    heapq.heappush(minHeap, (max(currentTime, grid[y - 1][x]), (y - 1, x)))

        return 0
