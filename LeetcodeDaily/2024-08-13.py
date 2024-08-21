class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        retvals = []
        currentArr = []
        self.helper(0, target, retvals, currentArr, 0, candidates)
        return retvals
        
    def helper(self, currentSum, target, retvals, currentArr, currentIndex, nums):
        if currentSum > target:
            return
        if currentSum == target:
            retvals.append(currentArr)
            return
        if currentIndex > len(nums) - 1:
            return
        self.helper(currentSum + nums[currentIndex], target, retvals, currentArr + [nums[currentIndex]], currentIndex + 1, nums)
        newIndex = currentIndex + 1
        while newIndex < len(nums) and nums[newIndex] == nums[currentIndex]:
            newIndex += 1
        self.helper(currentSum, target, retvals, currentArr, newIndex, nums)
