class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # put all elements in max heap
        # each time, add largest
        # divide by 3 and add back to max heap

        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            heapq.heappush(maxHeap, -1 * num)

        retval = 0
        for i in range(k):
            largest = heapq.heappop(maxHeap) * -1
            retval += largest
            largest = math.ceil(largest / 3)
            heapq.heappush(maxHeap, largest * -1)

        return retval
        
