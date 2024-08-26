#
# sliding window, we keep track of the bits in any window by taking the bitwise or
#

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        windowSize = 1
        longest = 1
        aggregatedBits = nums[0]
        for i in range(1, len(nums)):
            if aggregatedBits & nums[i] == 0:
                windowSize += 1
                longest = max(longest, windowSize)
                aggregatedBits = aggregatedBits | nums[i]
            else:
                windowSize = 1
                aggregatedBits = nums[i]
                for j in range(i - 1, - 1, - 1):
                    if aggregatedBits & nums[j] == 0:
                        windowSize += 1
                        aggregatedBits = aggregatedBits | nums[j]
                    else:
                        break
        return longest
