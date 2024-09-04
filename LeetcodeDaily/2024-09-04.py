#
# use an accumulator pattern of sorts - keep track of sum as we go, assign
# ranges in the sum to values
#

class Solution:

    def __init__(self, w: List[int]):
        regionMap = {}
        sum = 0
        for index, weight in enumerate(w):
            sum += weight
            regionMap[index] = (sum, index)
        self.regionMap = regionMap
        self.sum = sum

    def pickIndex(self) -> int:
        randomNum = random.random() * self.sum
        for i in range(len(self.regionMap.keys())):
            (region, index) = self.regionMap[i]
            if randomNum <= region:
                return index

        return 0


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
