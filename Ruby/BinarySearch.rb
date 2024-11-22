# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    left = 0
    right = nums.length - 1
    while left <= right
        middle = (left + right) / 2
        value = nums[middle]
        if target == value
            return middle
        elsif target < value
            right = middle - 1
        else
            left = middle + 1
        end
    end

    return -1
end
