inputArray = []
safeReports = 0

file = File.open("dec2.txt")
file.each_line do |line|
  line = line.split.map(&:to_i)

  isValid = true
  
  equal = 0
  increasing = 0
  decreasing = 0
  invalid = 0
  removed = 0

  reportLength = line.length

  i = 0
  while i < line.length - 1
    if line[i] == line[i+1] or (line[i] - line[i+1]).abs > 3
      line.delete_at(i)
      removed += 1
      i -= 1
    elsif line[i] < line[i+1]
      increasing += 1
      i += 1
    else
      decreasing += 1
      i += 1
    end

    if (decreasing + removed > 1 and increasing + removed > 1)
      isValid = false
      break
    end

  end

  if isValid
    print line
    safeReports += 1
  end

end

print safeReports
