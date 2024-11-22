# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    seen_dict = Hash.new(0)
    nums.each_with_index do |num, index|
        if seen_dict.key?(target - num)
            return [seen_dict[target - num], index]
        end
        seen_dict[num] = index
    end

    return []
end
