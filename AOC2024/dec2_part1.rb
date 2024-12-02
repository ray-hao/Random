inputArray = []
safeReports = 0

file = File.open("dec2.txt")
file.each_line do |line|
  line = line.split.map(&:to_i)
  isIncreasing = line[-1] > line[0]
  isValid = true
  (0...line.length - 1).each do |i|
    if (isIncreasing && (line[i + 1] <= line[i] or line[i+1] - line[i] > 3)) or ((not isIncreasing) && (line[i + 1] >= line[i] or line[i] - line[i+1] > 3))
      isValid = false
      break
    end
  end

  if isValid
    safeReports += 1
  end

end

print safeReports
