class Solution:
    def minimumSteps(self, s: str) -> int:
        dp = [0] * len(s)

        whites = 0

        for i, char in enumerate(s):
            if char == "0":
                dp[i] = dp[i - 1] + i - whites
                whites += 1
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
            
