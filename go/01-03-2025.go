func applyOperations(nums []int) []int {
    for idx, _ := range nums {
        if (idx == len(nums) - 1) {
            break
        }
        if nums[idx] == nums[idx + 1] {
            nums[idx] = nums[idx] * 2
            nums[idx + 1] = 0
        }
    }
    originalLen := len(nums)
    left := 0
    for left < len(nums) {
        if nums[left] == 0 {
            nums = append(nums[:left], nums[left + 1:]...)
        } else {
            left++
        }
    }

    nums = append(nums, make([]int, originalLen - len(nums))...)

    return nums

}
