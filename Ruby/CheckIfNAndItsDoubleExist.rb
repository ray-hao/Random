# @param {Integer[]} arr
# @return {Boolean}
def check_if_exist(arr)
    seenHash = Hash.new
    arr.each do |num|
        if seenHash.key?(num * 2) or (num % 2 == 0 and seenHash.key?(num / 2))
            return true
        end
        seenHash[num] = true
    end

    return false
end
