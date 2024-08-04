#
# to start let's just follow instructions first and compute all subarray sums, and sort it, and return sum between indices
#


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraySums = []
        for i in range(len(nums)):
            currentSum = nums[i]
            for j in range(i + 1, len(nums)):
                subarraySums.append(currentSum)
                currentSum += nums[j]
            subarraySums.append(currentSum)

        subarraySums.sort()
        retval = 0
        for i in range(left - 1, right):
            retval += subarraySums[i]
        return retval % (10**9 + 7)
