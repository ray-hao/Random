class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        return self.helper(0, 0, m, n, memo)

    def helper(self, currentPosX, currentPosY, m, n, memo):

        if (currentPosX, currentPosY) in memo:
            return memo[(currentPosX, currentPosY)]

        if currentPosX == n - 1 and currentPosY == m - 1:
            return 1

        if currentPosX > n - 1 or currentPosY > m - 1:
            return 0
        
        rightFirst = self.helper(currentPosX + 1, currentPosY, m, n, memo)
        downFirst = self.helper(currentPosX, currentPosY + 1, m, n, memo)
        
        memo[(currentPosX, currentPosY)] = rightFirst + downFirst

        return rightFirst + downFirst
