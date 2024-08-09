class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        vals = []
        amount = 2
        vals.append([rStart, cStart])
        # go right one
        cStart += 1
        if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
            vals.append([rStart, cStart])
        # go down one
        rStart += 1
        if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
            vals.append([rStart, cStart])

        leftUp = True
        while (len(vals) < rows * cols):
            if leftUp:
                for i in range(amount):
                    cStart -= 1
                    if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
                        vals.append([rStart, cStart])
                for i in range(amount):
                    rStart -= 1
                    if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
                        vals.append([rStart, cStart])
                leftUp = False
            else:
                for i in range(amount):
                    cStart += 1
                    if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
                        vals.append([rStart, cStart])
                for i in range(amount):
                    rStart += 1
                    if rStart < rows and cStart < cols and rStart >= 0 and cStart >= 0:
                        vals.append([rStart, cStart])
                leftUp = True
            amount += 1

        return vals
