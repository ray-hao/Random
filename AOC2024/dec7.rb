def testValid(goal, inputs, currentInput, currentValue)

  if currentValue > goal
    return false
  end
  
  if currentInput == inputs.length 
    if currentValue == goal
      return true
    end
    return false
  end

  sum = testValid(goal, inputs, currentInput + 1, currentValue + inputs[currentInput])
  
  if sum
    return true
  end

  if currentInput == 0
    return false
  end

  product = testValid(goal, inputs, currentInput + 1, currentValue * inputs[currentInput])

  if product
    return true
  end

  concat = testValid(goal, inputs, currentInput + 1, (currentValue.to_s + inputs[currentInput].to_s).to_i)

  if concat
    return true
  end

  return false

end

file = File.open("dec7.txt")

tests = []

retval = 0

file.each_line do |line|
  numbers = line.split(":")
  target = numbers[0].to_i
  input = numbers[1].split(" ")
  input.each_with_index do |val, index|
    input[index] = val.to_i
  end
  if testValid(target, input, 0, 0)
    retval += target.to_i
  end
end

print retval
