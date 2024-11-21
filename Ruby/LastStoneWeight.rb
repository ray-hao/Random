def binary_insert(stones, stone)
    left = 0
    right = stones.length - 1
    while left <= right
        middle = ((left + right) / 2).floor
        val = stones[middle]
        if stone == val
            stones.insert(middle, stone)
            return
        elsif stone > val
            left = middle + 1
        else
            right = middle - 1
        end
    end

    stones.insert(left, stone)
end

# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
    stones.sort!
    while stones.length > 1 do 
        first = stones.pop
        second = stones.pop
        new_stone = [first, second].max - [first, second].min

        binary_insert(stones, new_stone)
    end

    return stones[0]
end
