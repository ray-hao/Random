#
# we have some page ordering X | Y, which means that X must be printed before Y
# we need to verify orderings a, b, c, d to make sure that they follow the rules given
# which data structure should we use to keep track of order rules? It should support ordering, and read-heavy operations
#

require 'set'

file = File.open("dec5.txt")
rules = []
orderings = []
isRule = true
file.each_line do |line|
  if line == "\n"
    isRule = false
    next
  end

  if isRule
    rules << line
  else
    orderings << line
  end
end

nodes = Hash.new { |h, k| h[k] = Set.new() }

rules.each do |rule|
  first, second = rule.split("|")
  second = second.delete("\n")
  nodes[first].add(second)
end

retval = 0

orderings.each do |ordering|
  ordering = ordering.delete("\n")
  numbers = ordering.split(",")
  
  isValid = true
  numbers.each_with_index do |num, index|
    if index == numbers.length - 1
      next
    end

    (index + 1..numbers.length - 1).each do |nextIndex|
      if nodes[numbers[nextIndex]].include?(num)
        isValid = false
        break
      end
    end

    if not isValid
      break
    end

  end

  if isValid
    retval += numbers[numbers.length / 2].to_i
  end

end

print retval
