# @param {Integer} n
# @return {Integer}
def climb_stairs(n)

    if (n == 1)
        return 1
    elsif (n == 2) 
        return 2
    end 
    
    dp = Array.new(n) { |z| 0 }
    dp[0] = 1
    dp[1] = 2

    (2...n).each do |step|
        dp[step] = dp[step - 2] + dp[step - 1]
    end

    dp[-1]
    
end
