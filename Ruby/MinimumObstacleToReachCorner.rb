# @param {Integer[][]} grid
# @return {Integer}
def minimum_obstacles(grid)
    minHeap = MinHeap.new()
    rows = grid.length
    columns = grid[0].length
    remove_cost = rows * columns
    dp = Array.new(rows) { Array.new(columns) {1/0.0} }
    # [cost, x, y]
    minHeap.push(0, [0, 0, 0])
    dp[0][0] = 0
    while true
        current = minHeap.pop
        cost, x, y = current
        if x == rows - 1 and y == columns - 1
            return cost / remove_cost
        end

        # need to go up, down, left, right if possible. Also if there's a grid, we need to add 
        if x < rows - 1
            if grid[x + 1][y] == 1
                if cost + remove_cost < dp[x + 1][y]
                    minHeap.push(cost + remove_cost, [cost + remove_cost, x + 1, y])
                    dp[x + 1][y] = cost + remove_cost
                end
            else
                if cost < dp[x + 1][y]
                    minHeap.push(cost, [cost, x + 1, y])
                    dp[x + 1][y] = cost
                end
            end
        end

        if x > 0
            if grid[x - 1][y] == 1
                if cost + remove_cost < dp[x - 1][y]
                    minHeap.push(cost + remove_cost, [cost + remove_cost, x - 1, y])
                    dp[x - 1][y] = cost + remove_cost
                end
            else
                if cost < dp[x - 1][y]
                    minHeap.push(cost, [cost, x - 1, y])
                    dp[x - 1][y] = cost
                end
            end
        end

        if y > 0
            if grid[x][y - 1] == 1
                if cost + remove_cost < dp[x][y - 1]
                    minHeap.push(cost + remove_cost, [cost + remove_cost, x, y - 1])
                    dp[x][y - 1] = cost + remove_cost
                end
            else
                if cost < dp[x][y - 1]
                    minHeap.push(cost, [cost, x, y - 1])
                    dp[x][y - 1] = cost
                end
            end
        end

        if y < columns - 1
            if grid[x][y + 1] == 1
                if cost + remove_cost < dp[x][y + 1]
                    minHeap.push(cost + remove_cost, [cost + remove_cost, x, y + 1])
                    dp[x][y + 1] = cost + remove_cost
                end
            else
                if cost < dp[x][y + 1]
                    minHeap.push(cost, [cost, x, y + 1])
                    dp[x][y + 1] = cost
                end
            end
        end

    end

end
