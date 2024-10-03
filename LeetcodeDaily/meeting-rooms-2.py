class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        maxRooms = 1
        monoStack = []
        for interval in intervals:
            [startTime, endTime] = interval
            while len(monoStack) > 0 and monoStack[0] <= startTime:
                monoStack.pop(0)
            maxRooms = max(maxRooms, len(monoStack) + 1)

            currentIndex = 0
            while currentIndex < len(monoStack) and endTime > monoStack[currentIndex]:
                currentIndex += 1
            
            monoStack.insert(currentIndex, endTime)

        return maxRooms
