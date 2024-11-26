# @param {Integer[]} arr
# @return {Integer}
def fixed_point(arr)
    smallest = 1.0/0
    left = 0
    right = arr.length - 1
    while left <= right do
        middle = (left + right) / 2
        value = arr[middle]
        if middle == value
            smallest = middle
            right = middle - 1
        elsif middle > value
            left = middle + 1
        else
            right = middle - 1
        end
    end

    if smallest == 1/0.0
        return -1
    else
        return smallest
    end

end
