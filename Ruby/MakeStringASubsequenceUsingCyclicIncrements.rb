# @param {String} str1
# @param {String} str2
# @return {Boolean}
def can_make_subsequence(str1, str2)
    ptr1 = 0
    ptr2 = 0

    while ptr1 < str1.length and ptr2 < str2.length
        if str1[ptr1].ord == str2[ptr2].ord or str1[ptr1].ord + 1 == str2[ptr2].ord or (str1[ptr1] == "z" and str2[ptr2] == "a")
            ptr2 += 1
        end

        ptr1 += 1 
    end

    if ptr2 == str2.length
        return true
    else
        return false
    end

end
