#
# You have n + m trials.
# but n went missing, m observed.
# You have the average of the n + m trials.
#

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rollSum = 0
        for roll in rolls:
            rollSum += roll
        
        totalSum = (len(rolls) + n) * mean
        remainingSum = totalSum - rollSum
        
        # we have the remainingSum, we need to create remainingSum in an array of length n
        
        # It's impossible
        if remainingSum < n or remainingSum > 6 * n:
            return []

        # Construct it quickly, we know it's possible and each value is at least avg, and we can add one at a time knowing we'll hit the final desired value
        avg = math.floor(remainingSum / n)
        retval = [avg] * n
        remainingLeft = remainingSum - math.floor(remainingSum / n) * n
        index = 0
        while (remainingLeft != 0):
            retval[index] += 1
            index += 1
            remainingLeft -= 1


        return retval
