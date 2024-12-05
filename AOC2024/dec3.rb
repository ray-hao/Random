file = File.read("dec3.txt")
occurences = file.scan(/mul\((\d{1,3})\,(\d{1,3})\)|(don't\(\))|(do\(\))/)
enabled = true
retval = 0
occurences.each do |first, second, third, fourth|
  if third == "don't()"
    enabled = false
  elsif fourth == "do()"
    enabled = true
  elsif first and second and enabled
    retval += first.to_i * second.to_i
  else
    next
  end
end

print retval
