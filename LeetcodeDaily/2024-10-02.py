class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        seen = set()
        heap = []
        heapq.heapify(heap)
        total = 0
        for num in arr:
            if num not in seen:
                total += 1
                heapq.heappush(heap, -1 * num)
            seen.add(num)

        rankDict = {}
        while (len(heap) > 0):
            popped = heapq.heappop(heap) * -1
            rankDict[popped] = total
            total -= 1

        print(rankDict)

        retval = []
        for num in arr:
            retval.append(rankDict[num])

        return retval
        
