func findDifferentBinaryString(nums []string) string {
    // initial approach is to make dict to check presence, construct all 2^n, checking as we go
    dict := make(map[string]bool)
    for _, num := range nums {
        dict[num] = true
    }
    val, _ := helper("", len(nums[0]), dict)
    return val
}

func helper(currStr string, n int, dict map[string]bool) (string, bool) {
    if (len(currStr) == n) {
        _, ok := dict[currStr]
        if !ok {
            return currStr, true
        } 
        return currStr, false
    }

    strVal, valid := helper(currStr + "0", n, dict)
    if valid {
        return strVal, true
    }

    strVal, valid = helper(currStr + "1", n, dict)
    if valid {
        return strVal, true
    }

    return "", false
}
