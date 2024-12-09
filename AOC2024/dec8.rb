file = File.open("dec8.txt")
nodeMap = Hash.new { |h,k| h[k] = [] }

rows = 0
cols = 0

file.each_with_index do |line, y|
  rows += 1
  line = line.delete("\n")
  line.chars.each_with_index do |char, x|
    if rows == 1
      cols += 1
    end

    if char != "."
      nodeMap[char].push([x, y])
    end
  end
end

retval = 0
antinodes = []

(0...rows).each do |_|
  antinodes.push(Array.new(cols, 0))
end

nodeMap.keys.each do |key|
  nodes = nodeMap[key]
  nodes.each do |node1|
    nodes.each do |node2|
      if node1 == node2
        next
      else
        deltaY = node2[1] - node1[1]
        deltaX = node2[0] - node1[0]
        nextNodeX = node2[0] + deltaX
        nextNodeY = node2[1] + deltaY

        if nextNodeX < cols and nextNodeY < rows and nextNodeX >= 0 and nextNodeY >= 0 and antinodes[nextNodeX][nextNodeY] == 0
          antinodes[nextNodeX][nextNodeY] = 1
          retval += 1
        end
      end

    end
  end
end

print retval
