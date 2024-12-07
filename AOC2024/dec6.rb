file = File.open("dec6.txt")

map = []

x = 0
y = 0
# 0 => up, 1 => right, 2 => down, 3 => left
currentDir = 0

rows = 0
columns = 0

counter = 0

file.each_with_index do |line, row|
  rows += 1
  currentRow = []
  rowLine = line.delete("\n")
  rowLine.chars.each_with_index do |char, col|
    if rows == 1
      columns += 1
    end

    if char == "^"
      x = row
      y = col
      currentRow.push("X")
      counter += 1
    else
      currentRow.push(char)
    end
  end
  map.push(currentRow)
end

while true

  nextX = x
  nextY = y

  if currentDir == 0
    nextX -= 1
  elsif currentDir == 1
    nextY += 1
  elsif currentDir == 2
    nextX += 1
  else
    nextY -= 1
  end

  if nextX >= rows or nextY >= columns or nextX < 0 or nextY < 0
    break
  elsif map[nextX][nextY] == "."
    counter += 1
    map[nextX][nextY] = "X"
    x = nextX
    y = nextY
  elsif map[nextX][nextY] == "X"
    x = nextX
    y = nextY
  elsif map[nextX][nextY] == "#"
    currentDir = (currentDir + 1) % 4
  end

end

print counter
