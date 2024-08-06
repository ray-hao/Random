#
# we can use 2 - 9 (8 numbers) to map 26 letters
# the first 1 - 8 should be press once, 9 - 16 press twice, 
# 17 - 24 three times, 25 - 26 four times
#

class Solution:
    def minimumPushes(self, word: str) -> int:
        letters = defaultdict(lambda: 0)
        for char in word:
            letters[char] += 1

        vals = []

        for key, value in letters.items():
            vals.append(value)

        vals.sort(reverse=True)

        num = 1
        presses = 0
        for val in vals:
            if num <= 8:
                presses += 1 * val
            elif num <= 16:
                presses += 2 * val
            elif num <= 24:
                presses += 3 * val
            else:
                presses += 4 * val
            num += 1

        return presses


        return 0
