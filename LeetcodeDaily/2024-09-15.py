#
# given array nums of size n
#
# maximum subarray with maximum bitwise AND
#
# isn't it just the longest subarray of the largest number?
# because if we bitwise and a smaller number, it won't be the max possible bitwise and anymore
#

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        retval = 0
        maxVal = nums[0]
        current = 0
        for num in nums:
            if num == maxVal:
                current += 1
            elif num < maxVal:
                current = 0
            elif num > maxVal:
                retval = 0
                current = 1

            maxVal = max(maxVal, num)
            retval = max(retval, current)

        return retval
        # maxVal = 0
        # for num in nums:
        #     maxVal = max(maxVal, num)

        # longest = 0
        # current = 0
        # counter = 0
        # while (current < len(nums)):
            
        #     if (nums[current] == maxVal):
        #         counter += 1
        #     else:
        #         counter = 0

        #     longest = max(longest, counter)
        #     current += 1
        
        # return longest
