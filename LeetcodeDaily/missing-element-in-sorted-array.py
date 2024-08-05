# O(logn) solution
#
# ok so we know we need to do some binary search thing.
# given any 2 indices, we know how many elements are missing in between
# them by subtracting their values, and subtracting the differences in indices
#
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = math.floor((left + right) / 2)
            leftVal = nums[left]
            rightVal = nums[right]
            middleVal = nums[middle]
            missingLeft = middleVal - leftVal - 1 - (middle - left - 1)
            missingRight = rightVal - middleVal - 1 - (right - middle - 1)
            # if the missing val we want is bigger than the number of missing values in left half
            if k >= missingLeft:
                k -= missingLeft
                if k == 0:
                    right = middle
                if middle < len(nums) - 1:
                    if k - (nums[middle + 1] - nums[middle] - 1) > 0:
                        k -= nums[middle + 1] - nums[middle] - 1
                        left = middle + 1
                    elif k - (nums[middle + 1] - nums[middle] - 1) == 0:
                        left = middle
                        break
                    else:
                        left = middle
                        break
                else:
                    break
            else:
                right = middle - 1

        if k > 0:
            if left < len(nums):
                return nums[left] + k
            else:
                return nums[-1] + k
        else:
            targetVal = nums[left]
            index = left
            while (targetVal == nums[index]):
                targetVal -= 1
                index -= 1
            return targetVal

# O(n) solution
# class Solution:
#     def missingElement(self, nums: List[int], k: int) -> int:
        # O(n) solution below
        #
        # for i in range(len(nums) - 1):
        #     currentDiff = nums[i + 1] - nums[i] - 1
        #     if k >= currentDiff:
        #         k -= currentDiff
        #         if k == 0 and currentDiff >= 1:
        #             return nums[i] + currentDiff
        #     else:
        #         return nums[i] + k
        # if k == 0:
        #     return nums[-1] + 1
        # return nums[-1] + k

        
