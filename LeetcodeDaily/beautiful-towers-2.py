#
# can we just look at each tower individually and expand outwards greedily?
#
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maxTotal = float('-inf')
        for i in range(len(maxHeights)):
            total = maxHeights[i]
            minLeft = maxHeights[i]
            minRight = maxHeights[i]
            for left in range(i - 1, - 1, - 1):
                minLeft = min(minLeft, maxHeights[left])
                total += minLeft
            for right in range(i + 1, len(maxHeights)):
                minRight = min(minRight, maxHeights[right])
                total += minRight
            maxTotal = max(maxTotal, total)
        return maxTotal
            
