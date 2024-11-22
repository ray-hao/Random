# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    myDict = {}
    nums.each do |num|
        if myDict.key?(num)
            return true
        end
        myDict[num] = 1
    end
    return false
end
