func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
    ptr1 := 0
    ptr2 := 0
    mergedResult := make([][]int, 0)

    for ptr1 < len(nums1) || ptr2 < len(nums2) {
        if ptr1 >= len(nums1) {
            currentEntry := nums2[ptr2]
            mergedResult = append(mergedResult, currentEntry)
            ptr2++
        } else if ptr2 >= len(nums2) {
            currentEntry := nums1[ptr1]
            mergedResult = append(mergedResult, currentEntry)
            ptr1++
        } else {
            entry1 := nums1[ptr1]
            entry2 := nums2[ptr2]
            if entry1[0] == entry2[0] {
                mergedResult = append(mergedResult, []int{entry1[0], entry1[1] + entry2[1]})
                ptr1++
                ptr2++
            } else if entry1[0] > entry2[0] {
                mergedResult = append(mergedResult, entry2)
                ptr2++
            } else {
                mergedResult = append(mergedResult, entry1)
                ptr1++
            }
        }
    }

    return mergedResult
}
