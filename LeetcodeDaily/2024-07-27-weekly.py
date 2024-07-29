# the i-th coin has probability prob[i] of facing heads when tossed
# what is the probablility that the number of coins facing heads is target when all are thrown together?

#
# let's use a 2d array to keep track of the probability of getting t heads by the time we throw our xth throws.
#
# ex. [0][0] is probability we have 0 heads on our first roll, [3][5] is the probability we have 3 heads by our 6thth roll
#


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0] * len(prob) for i in range(target + 1)]
        # we can fill this array out row by row, top to bottom. Our answer will be in dp[-1][-1]

        dp[0][0] = 1 - prob[0]
        for p in range(1, len(prob)):
            dp[0][p] = dp[0][p - 1] * (1 - prob[p])
                
        runningProb = 1
        if len(dp) > 1:
            for p in range(len(prob)):
                dp[1][p] = runningProb * prob[p]
                if p >= 1:
                    dp[1][p] += dp[1][p - 1] * (1 - prob[p])
                runningProb *= (1 - prob[p])

        for row in range(2, target + 1):
            for column in range(row - 1, len(prob)):
                dp[row][column] = dp[row - 1][column - 1] * prob[column] + dp[row][column - 1] * (1 - prob[column])

        return dp[-1][-1]
