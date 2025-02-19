func getHappyString(n int, k int) string {
    // for a string of length n, we have 3 * 2 ^ (n - 1) happy strings
    kindex := k

    twos := 1 << (n - 1)

    if kindex > 3 * twos {
        return ""
    }

    strBuilder := ""
    lower := 1
    upper := 3 * twos 

    if k > 0 && k <= twos  {
        upper = twos
        strBuilder += "a"
    } else if k > twos  && k <= 2 * twos  {
        lower = twos + 1
        upper = 2 * twos       
        strBuilder += "b"
    } else {
        lower = 2 * twos + 1
        strBuilder += "c"
    }

    for lower < upper {
        lastChar := strBuilder[len(strBuilder) - 1:]
        if k >= lower && k <= lower + (upper - lower) / 2 {
            if lastChar == "a" {
                strBuilder += "b"
            } else {
                strBuilder += "a"
            }
            upper = lower + (upper - lower) / 2
        } else {
            if lastChar == "c" {
                strBuilder += "b"
            } else {
                strBuilder += "c"
            }
            lower = lower + (upper - lower) / 2 + 1
        }
    }

    fmt.Println(lower, upper)
    return strBuilder

    // let's say we're given some valid k
    // if k is in [0, 2 ^ (n - 1)) then it starts with 'a'
    // if k is in [2 ^ (n - 1), 2 * 2 ^ (n - 1)) then it starts with 'b'
    // ...
    // then if its in upper half, it's the larger of the options
    // otherwise, it's the smaller of the options, keep adjusting bounds
    
    //  1   2   3   4
    // aba abc aca acb

}
