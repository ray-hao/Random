#
# people take the smallest unoccupied chair (needs to stay sorted)
# sort by arrival time, but also keep track of leaving time
# we only care about people that arrive before the targetFriend's arrival time
#

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        targetArrivalTime = times[targetFriend][0]
        def filterFn(num):
            return num[0] <= targetArrivalTime

        relevantTimes = list(filter(filterFn, times))
        relevantTimes.sort(key = lambda x: x[0])

        chairsMinHeap = []
        endTimesHeap = []

        heapq.heapify(chairsMinHeap)
        heapq.heapify(endTimesHeap)

        for i in range(len(relevantTimes)):
            heapq.heappush(chairsMinHeap, i)
        
        while (len(relevantTimes) > 0):
            [currentFriendStart, currentFriendEnd] = relevantTimes.pop(0)
            while (len(endTimesHeap) > 0 and endTimesHeap[0][0] <= currentFriendStart):
                [endTime, chair] = heapq.heappop(endTimesHeap)
                heapq.heappush(chairsMinHeap, chair)
            
            currentFriendChair = heapq.heappop(chairsMinHeap)
            heapq.heappush(endTimesHeap, [currentFriendEnd, currentFriendChair])

            if len(relevantTimes) == 0:
                return currentFriendChair


        return 0

        
