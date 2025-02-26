func numOfSubarrays(arr []int) int {
    total := 0
    currentSum := 0
    seenEvens := 1
    seenOdds := 0

    for _, val := range arr {
        currentSum += val
        if currentSum % 2 == 0 {
            total += seenOdds
            seenEvens += 1
        } else {
            total += seenEvens
            seenOdds += 1
        }
    }

    return total % (int(math.Pow(10, 9)) + 7)

}
