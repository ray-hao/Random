#
# ok so in this question we can find all 3x3 subgrids, and check each one individually. Let's implement this and go from there.
#

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid) - 2):
            for column in range(len(grid[0]) - 2):
                if self.checkMagicSquare(grid, row, column):
                    count += 1
        
        return count

    def checkMagicSquare(self, grid, topLeftSquareX, topLeftSquareY):
        seenNums = set()
        # checkRows and uniqueness
        for i in range(3):
            currentSum = 0
            for j in range(3):
                if grid[topLeftSquareX + i][topLeftSquareY + j] in seenNums or grid[topLeftSquareX + i][topLeftSquareY + j] <= 0 or grid[topLeftSquareX + i][topLeftSquareY + j] >= 10:
                    return False
                seenNums.add(grid[topLeftSquareX + i][topLeftSquareY + j])
                currentSum += grid[topLeftSquareX + i][topLeftSquareY + j]
            if currentSum != 15:
                return False

        # checkColumns
        for i in range(3):
            currentSum = 0
            for j in range(3):
                currentSum += grid[topLeftSquareX + j][topLeftSquareY + i]
            if currentSum != 15:
                return False

        # checkDiagonals
        leftToRightDiagonal = 0
        rightToLeftDiagonal = 0
        for i in range(3):
            leftToRightDiagonal += grid[topLeftSquareX + i][topLeftSquareY + i]
            rightToLeftDiagonal += grid[topLeftSquareX + i][topLeftSquareY + 2 - i]
        if leftToRightDiagonal != 15 or rightToLeftDiagonal != 15:
            return False

        return True        

