#
# probably just backtrack, while keeping track of seen nums using set and
# keeping track of transitions using dict (currentNum -> nextNum : [])
#

class Solution:
    nextNumbers = {
        1: [2, 5, 4, 6, 8],
        2: [1, 4, 5, 6, 3, 7, 9],
        3: [2, 5, 6, 4, 8],
        4: [1, 2, 5, 7, 8, 9, 3],
        5: [1, 2, 3, 4, 6, 7, 8, 9],
        6: [3, 5, 9, 2, 8, 1, 7],
        7: [4, 5, 8, 2, 6],
        8: [7, 4, 5, 6, 9, 1, 3],
        9: [8, 5, 6, 4, 2],
    }

    jumps = {
        1: [(3, 2), (9, 5), (7, 4)],
        2: [(8, 5)],
        3: [(1, 2), (7, 5), (9, 6)],
        4: [(6, 5)],
        5: [],
        6: [(4, 5)],
        7: [(1, 4), (3, 5), (9, 8)],
        8: [(2, 5)],
        9: [(3, 6), (1, 5), (7, 8)],

    }

    def numberOfPatterns(self, m: int, n: int) -> int:
        seen = set()
        retval = 0
        for i in range(1, 10):
            seen.add(i)
            retval += self.helper(seen, i, m, n)
            seen.remove(i)
        return retval

    def helper(self, seen, currentNum, min, max):
        currentLength = len(seen)
        retval = 0
        if currentLength >= min and currentLength <= max:
            retval += 1
        
        if currentLength == max:
            return retval

        nextOptions = self.nextNumbers[currentNum]
        jumpOptions = self.jumps[currentNum]
        for option in nextOptions:
            if option in seen:
                continue
            seen.add(option)
            retval += self.helper(seen, option, min, max)
            seen.remove(option)
         
        for jump in jumpOptions:
            nextOption = jump[0]
            intermediate = jump[1]

            if nextOption in seen or intermediate not in seen:
                continue
            seen.add(nextOption)
            retval += self.helper(seen, nextOption, min, max)
            seen.remove(nextOption)

        return retval
