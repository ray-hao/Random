# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    if s.length != t.length
        return false
    end

    chars_dict = Hash.new(0)
    s.chars.each do |char|
        chars_dict[char] += 1
    end
    t.chars.each do |char|
        chars_dict[char] -= 1
    end

    chars_dict.keys.each do |key|
        if chars_dict[key] != 0
            return false
        end
    end

    return true

end
