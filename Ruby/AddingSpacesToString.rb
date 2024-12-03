# @param {String} s
# @param {Integer[]} spaces
# @return {String}
def add_spaces(s, spaces)
    counter = 0
    spaces.each do |space|
        s.insert(space + counter, " ")
        counter += 1
    end

    return s 
end
