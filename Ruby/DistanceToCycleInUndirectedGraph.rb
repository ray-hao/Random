class Node

    attr_accessor :value, :neighbors

    def initialize(value, neighbors = [])
        @value = value
        @neighbors = neighbors
    end

end

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def distance_to_cycle(n, edges)
    graphNodes = []
    (0...n).each do |n|
        new_node = Node.new(n)
        graphNodes.push(new_node)
    end

    graphEdges = Hash.new { |h,k| h[k] = 0 }

    edges.each do |edge|
        node1, node2 = edge
        graphNodes[node1].neighbors.push(graphNodes[node2])
        graphNodes[node2].neighbors.push(graphNodes[node1])
        graphEdges[node1] += 1
        graphEdges[node2] += 1
    end

    tipNodes = []

    graphEdges.each do |key, value|
        if value == 1
            tipNodes.push(key)
        end
    end

    # let's try easy solution first: find the cycle, for each node in the cycle, run a BFS to get shortest path on each dangling tree connected to cycle

    tipNodes.each do |node|
        nodesToRemove = [node]
        while nodesToRemove.length != 0
            current = nodesToRemove.pop
            graphEdges[current] -= 1
            nodeNeighbors = graphNodes[current]
            nodeNeighbors.neighbors.each do |neighbor|
                graphEdges[neighbor.value] -= 1
                if graphEdges[neighbor.value] == 1
                    nodesToRemove.push(neighbor.value)
                end
            end
        end
    end

    cycleNodes = []
    graphNodes.each do |node|
        if graphEdges[node.value] == 2
            cycleNodes.push(node.value)
        end
    end

    shortest = Array.new(n, 1/0.0)

    seen = Hash.new

    cycleNodes.each do |node|
        queue = []
        queue.push([0, node])
        while queue.length != 0
            distance, node = queue.pop
            seen[node] = true
            shortest[node] = [shortest[node], distance].min
            graphNodes[node].neighbors.each do |neighbor|
                if not cycleNodes.include?(neighbor.value) and not seen.key?(neighbor.value)
                    queue.push([distance + 1, neighbor.value])
                end
            end
        end
    end

    return shortest
    
end
