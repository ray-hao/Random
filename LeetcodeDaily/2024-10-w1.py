class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        myDict = defaultdict(lambda : 0)
        heap = []
        heapq.heapify(heap)
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                heapq.heappush(heap, -1 * num)
            myDict[num] += 1

        while (len(heap) > 0):
            popped = heapq.heappop(heap) * -1
            if myDict[popped] == 1:
                return popped

        return -1
