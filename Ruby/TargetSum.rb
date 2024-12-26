# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def find_target_sum_ways(nums, target)
    
    def get_results(current_position, sum, nums, target, dict)

        if dict.include?([current_position, sum])
            return dict[[current_position, sum]]
        end

        if current_position == nums.length
            if sum == target
                return 1
            else
                return 0
            end
        end

        sum += nums[current_position]
        add = get_results(current_position + 1, sum, nums, target, dict)

        sum -= (nums[current_position] * 2)
        subtract = get_results(current_position + 1, sum, nums, target, dict)

        dict[[current_position, sum + nums[current_position]]] = add + subtract

        return add + subtract
    end

    dict = Hash.new
    return get_results(0, 0, nums, target, dict)

end
