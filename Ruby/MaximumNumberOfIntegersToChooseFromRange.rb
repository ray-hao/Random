# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
    banned = Set.new(banned)
    sum = 0
    count = 0
    (1..n).each do |num|
        if sum + num > max_sum
            break
        end

        if not banned.include?(num)
            sum += num
            count += 1
        end
    end

    return count
end
