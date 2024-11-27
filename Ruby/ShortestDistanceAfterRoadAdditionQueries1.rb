class Node

    attr_accessor :val, :neighbors

    def initialize(val = 0, neighbors = [])
        @val = val
        @neighbors = neighbors
    end
end

def get_shortest(nodes)
    if nodes.length == 0 or nodes.length == 1
        return 0
    end

    dp = Array.new(nodes.length, 1/0.0)
    dp[nodes.length - 1] = 0
    dp[nodes.length - 2] = 1
    (nodes.length - 3).downto(0).each do |index|
        node = nodes[index]
        neighbors = node.neighbors
        neighbors.each do |neighbor|
            dp[index] = [dp[index], 1 + dp[neighbor]].min
        end
    end

    return dp[0]
end

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
    retval = []
    nodes = Array.new(n)
    (0...n).each do |num|
        new_node = Node.new(num)
        if num < n - 1
            new_node.neighbors.push(num + 1)
        end
        nodes[num] = new_node
    end

    queries.each do |query|
        origin, dest = query
        nodes[origin].neighbors.push(dest)
        retval.push(get_shortest(nodes))
    end

    return retval

end
