class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        indices = [0] * len(nums)
        minheap = []
        heapq.heapify(minheap)
        rangeMin = float('inf')
        rangeMax = float('-inf')
        for i in range(len(nums)):
            rangeMin = min(rangeMin, nums[i][0])
            rangeMax = max(rangeMax, nums[i][0])
            heapq.heappush(minheap, (nums[i][0], i))
        
        idealRange = [rangeMin, rangeMax]

        while True:
            [poppedNum, poppedList] = heapq.heappop(minheap)
            indices[poppedList] += 1
            if indices[poppedList] >= len(nums[poppedList]):
                return idealRange
            
            heapq.heappush(minheap, (nums[poppedList][indices[poppedList]], poppedList))
            rangeMax = max(rangeMax, nums[poppedList][indices[poppedList]])
            rangeMin = minheap[0][0]
            if rangeMax - rangeMin < idealRange[1] - idealRange[0]:
                idealRange = [rangeMin, rangeMax]

        
