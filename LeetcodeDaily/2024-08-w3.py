class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        gridSize = len(rooks)
        rows = [i for i in range(gridSize)]
        rookRows = [rook[1] for rook in rooks]
        rookRows.sort()

        cols = [i for i in range(gridSize)]
        rookCols = [rook[0] for rook in rooks]
        rookCols.sort()

        moves = 0

        for i in range(gridSize - 1, - 1, - 1):
            moves += abs(rows[i] - rookRows[i])
            moves += abs(cols[i] - rookCols[i])

        return moves
