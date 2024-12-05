file = File.open("dec4.txt")

wordSearch = []
file.each_line do |line|
  wordSearch.push(line)
end

occurences = 0

#
# Part 1
#
# wordSearch.each_with_index do |line, row|
#   line.chars.each_with_index do |char, col|
#     if char == "X"
#       # right
#       if col <= line.length - 1 - 3 and wordSearch[row][col + 1] == "M" and wordSearch[row][col + 2] == "A" and wordSearch[row][col + 3] == "S"
#         occurences += 1
#       end
#       # down
#       if row <= wordSearch.length - 1 - 3 and wordSearch[row + 1][col] == "M" and wordSearch[row + 2][col] == "A" and wordSearch[row + 3][col] == "S"
#         occurences += 1
#       end
#       # left
#       if col >= 3 and wordSearch[row][col - 1] == "M" and wordSearch[row][col - 2] == "A" and wordSearch[row][col - 3] == "S"
#         occurences += 1
#       end
#       # up
#       if row >= 3 and wordSearch[row - 1][col] == "M" and wordSearch[row - 2][col] == "A" and wordSearch[row - 3][col] == "S"
#         occurences += 1
#       end
#       # downRight
#       if row <= wordSearch.length - 4 and col <= line.length - 4 and wordSearch[row + 1][col + 1] == "M" and wordSearch[row + 2][col + 2] == "A" and wordSearch[row + 3][col + 3] == "S"
#         occurences += 1
#       end
#       # upRight
#       if row >= 3 and col <= line.length - 4 and wordSearch[row - 1][col + 1] == "M" and wordSearch[row - 2][col + 2] == "A" and wordSearch[row - 3][col + 3] == "S"
#         occurences += 1
#       end
#       # downLeft
#       if row <= wordSearch.length - 4 and col >= 3 and wordSearch[row + 1][col - 1] == "M" and wordSearch[row + 2][col - 2] == "A" and wordSearch[row + 3][col - 3] == "S"
#         occurences += 1
#       end
#       # upLeft
#       if row >= 3 and col >= 3 and wordSearch[row - 1][col - 1] == "M" and wordSearch[row - 2][col - 2] == "A" and wordSearch[row - 3][col - 3] == "S"
#         occurences += 1
#       end
#     end
#   end
# end

#
# Part 2
#
wordSearch.each_with_index do |line, row|
  line.chars.each_with_index do |char, col|
    if row == 0 or row == wordSearch.length - 1 or col == 0 or col == line.length - 1
      next
    end

    if char == "A"
      if (wordSearch[row - 1][col - 1] == "M" and wordSearch[row + 1][col + 1] == "S") or (wordSearch[row - 1][col - 1] == "S" and wordSearch[row + 1][col + 1] == "M")
        if wordSearch[row - 1][col + 1] == "M" and wordSearch[row + 1][col - 1] == "S"
          occurences += 1
        end
        if wordSearch[row - 1][col + 1] == "S" and wordSearch[row + 1][col - 1] == "M"
          occurences += 1
        end
      end
    end
  end
end

print occurences
