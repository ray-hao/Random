# @param {Integer[]} cost
# @return {Integer}
def min_cost_climbing_stairs(cost)
    dp = Array.new(cost.length + 1) { |z| 1/0.0 }
    dp[0] = 0
    dp[1] = 0
    (2..cost.length).each do |i|
        dp[i] = [dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]].min
    end

    dp[-1]
end
