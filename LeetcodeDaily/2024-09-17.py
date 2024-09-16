#
# we can just sort, and compare adjacent, and make sure to check the first against the last entry
#

class Solution:

    def getTimeInMinutes(self, time):
        return int(time[0:2]) * 60 + int(time[-2:])

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key=lambda x: (x[0: 2], x[-2:]))
        minDiff = float('inf')
        timePoints.append(timePoints[0])
        for i in range(len(timePoints) - 1):
            time1 = self.getTimeInMinutes(timePoints[i])
            time2 = self.getTimeInMinutes(timePoints[i + 1])
            diff = min(abs(time1 - time2), abs(time1 + 1440 - time2), abs(time1 - 1440 - time2))
            minDiff = min(minDiff, diff)

        return minDiff
      
