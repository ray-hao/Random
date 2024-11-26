# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def find_champion(n, edges)
    potentials = Array.new(n, false)
    edges.each do |edge|
        parent, child = edge
        potentials[child] = true
    end

    retval = []
    potentials.each_with_index do |is_root, index|
        if not is_root
            retval.push(index)
        end
    end

    if retval.length > 1 or retval.length == 0
        return -1
    else
        return retval[0]
    end

end
