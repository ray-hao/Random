class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # 0, 1, 2, 3 -> right, down, left, up
        dir = 0
        seen = 0
        total = len(matrix[0]) * len(matrix)
        currentX = 0
        currentY = 0
        seen = set()
        retval = []
        while (len(seen) != total):
            if (currentX, currentY) not in seen:
                seen.add((currentX, currentY))
                retval.append(matrix[currentY][currentX])

            if dir == 0:
                if currentX == right:
                    dir += 1
                    top += 1
                    continue
                else:
                    currentX += 1
                    continue

            if dir == 1:
                if currentY == bottom:
                    dir += 1
                    right -= 1
                    continue
                else:
                    currentY += 1
                    continue

            if dir == 2:
                if currentX == left:
                    dir += 1
                    bottom -= 1
                    continue
                else:
                    currentX -= 1
                    continue

            if dir == 3:
                if currentY == top:
                    dir = 0
                    left += 1
                    continue
                else:
                    currentY -= 1
                    continue

        return retval
