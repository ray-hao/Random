#
# once we get to a power of 2, we know the answer
#

class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        values = []
        memo = {}
        for i in range(10):
            memo[2 ** i] = int(math.log2(2 ** i))

        for val in range(lo, hi + 1):
            seen = []
            original = val
            counter = 0
            while val != 1:
                seen.append(val)
                counter += 1
                if val % 2 == 0:
                    val /= 2
                else:
                    val = val * 3 + 1

                if val in memo:
                        counter += memo[val]
                        break

            values.append((counter, original))
            for index, seenVal in enumerate(seen):
                memo[seenVal] = counter - index

        values.sort(key = lambda x: (x[0], x[1]))
        return values[k - 1][1]
