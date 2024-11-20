# @param {String} s
# @return {Boolean}

$CHARACTERS = ('a'..'z')
$NUMBERS = ('0'..'9')

def is_palindrome(s)
    left = 0
    right = s.length - 1
    while left <= right do
        unless $CHARACTERS.include?(s[left].downcase) || $NUMBERS.include?(s[left])
            left += 1
            next
        end

        unless $CHARACTERS.include?(s[right].downcase) || $NUMBERS.include?(s[right])      
            right -= 1
            next
        end

        if s[left].downcase != s[right].downcase
            return false
        end

        left += 1
        right -= 1
    end
    return true
    
end
