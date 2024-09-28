class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if len(self.intervals) == 0:
            self.intervals.append([start, end - 1])
            return True
        left = 0
        right = len(self.intervals) - 1
        while (left <= right):
            middle = math.floor((left + right) / 2)
            [existingStart, existingEnd] = self.intervals[middle]
            if existingStart >= start:
                right = middle - 1
            else:
                left = middle + 1

        expectedPosition = left
        
        if expectedPosition == 0:
            if (end - 1) < self.intervals[0][0]:
                self.intervals.insert(0, [start, end - 1])
                return True

        if start > self.intervals[expectedPosition - 1][1] and (left >= len(self.intervals) or (end - 1) < self.intervals[expectedPosition][0]):
            self.intervals.insert(expectedPosition, [start, end - 1])
            return True
        
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
