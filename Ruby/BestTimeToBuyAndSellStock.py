# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    max_profit = 0
    lowest = prices[0]
    highest = prices[0]
    prices.each do |price|
        lowest = [lowest, price].min
        highest = price
        max_profit = [max_profit, highest - lowest].max
    end

    return max_profit
end
