#
# first, let's just run the intuitive way: for each query, run the 
# XOR from l to r
#

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixSums = {}
        prefixSums[0] = 0
        current = arr[0]
        for i in range(1, len(arr)):
            prefixSums[i] = current
            current = current ^ arr[i]
        
        retval = []
        for query in queries:
            [left, right] = query
            if left == right:
                retval.append(arr[left])
            else:
                retval.append(prefixSums[left] ^ prefixSums[right] ^ arr[right])
        
        return retval
