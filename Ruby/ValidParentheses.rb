# @param {String} s
# @return {Boolean}
def is_valid(s)
    stack = Array.new()
    s.chars.each do |paren|
        if paren == "(" or paren == "[" or paren == "{"
            stack << paren
        else
            if (paren == ")" and stack[-1] == "(") or (paren == "]" and stack[-1] == "[") or (paren == "}" and stack[-1] == "{")
                stack.pop
            else
                return false
            end
        end
    end
    
    if stack.length == 0
        return true
    end

    return false
end
