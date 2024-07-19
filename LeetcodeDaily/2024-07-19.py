# just use the fact that each of the elements in matrix are unique

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minimums = set()
        for row in matrix:
            rowMin = float('inf')
            for num in row:
                rowMin = min(num, rowMin)
            minimums.add(rowMin)
        
        solutions = []
        for column in range(len(matrix[0])):
            colMax = float('-inf')
            for row in range(len(matrix)):
                colMax = max(colMax, matrix[row][column])
            if colMax in minimums:
                solutions.append(colMax)

        return solutions
