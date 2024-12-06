array1 = []
array2 = []

file = File.open("dec1.txt")
file.each_line do |line|
  num1, num2 = line.split.map(&:to_i)
  array1 << num1
  array2 << num2
end

array1.sort!
array2.sort!

diff = 0

array1.each_with_index do |num, index|
  diff += (array2[index] - num).abs
end

puts diff

# Part 2

# array1 = []
# array2 = []

# file = File.open("dec1.txt")

# occurences = Hash.new { |h, k| h[k] = 0}

# file.each_line do |line|
#   num1, num2 = line.split.map(&:to_i)
#   occurences[num2] += 1
#   array1 << num1
#   array2 << num2
# end

# similarity = 0
# array1.each do |num|
#   similarity += num * occurences[num]
# end

# puts similarity
