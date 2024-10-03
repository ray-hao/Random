class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        returnIntervals = []
        currentInterval = 0
        merging = False
        mergingStart = None
        mergingEnd = None
        while (currentInterval < len(intervals) - 1):
            
            [currentStart, currentEnd] = intervals[currentInterval]
            [nextStart, nextEnd] = intervals[currentInterval + 1]

            if currentEnd >= nextStart or (mergingEnd and mergingEnd >= nextStart): 
                if not merging:
                    merging = True
                    mergingStart = currentStart
                if mergingEnd:
                    mergingEnd = max(mergingEnd, nextEnd, currentEnd)
                else:
                    mergingEnd = max(currentEnd, nextEnd)
            else:
                if merging:
                    returnIntervals.append([mergingStart, mergingEnd])
                    merging = False
                else:
                    returnIntervals.append([currentStart, currentEnd])

            currentInterval += 1

        if merging:
            returnIntervals.append([mergingStart, mergingEnd])
        else:
            returnIntervals.append(intervals[currentInterval])

        return returnIntervals
    
