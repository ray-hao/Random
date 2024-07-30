#
# basically we know that at some point, we'll see the b that will be the first one in the balanced string.
# we want to delete all the b's before it, and all the a's after it.
#
# also if we see a subsequence of consecutive b's, we can skip after checking the first one, since the ones after the first
#  in the string of consecutive subsequence will be strictly worse.
#

class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        bBefore = []
        bCount = 0
        for char in s:
            bBefore.append(bCount)
            if char == 'b':
                bCount += 1

        aCount = len(s) - bCount
        aAfter = []
        for char in s:
            if char == 'a':
                aCount -= 1
            aAfter.append(aCount)

        minOps = float('inf')
        for index in range(len(s)):
            if index > 0 and s[index - 1] == 'b':
                continue
            if s[index] == 'b':
                minOps = min(minOps, aAfter[index] + bBefore[index])
        
        if minOps == float('inf'):
            return 0

        # if optimal is just deleting all b's
        return min(minOps, bCount)

