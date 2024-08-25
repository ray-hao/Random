class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        retvals = []
        self.helper(retvals, "", 0, word, 0)
        return retvals

    def helper(self, retvals, currentWord, currentNum, word, pos):
        if pos == len(word):
            if currentNum > 0:
                currentWord += str(currentNum)
            retvals.append(currentWord)
            return

        # place char
        if (currentNum > 0):
            self.helper(retvals, currentWord + str(currentNum) + word[pos], 0, word, pos + 1)
        else:
            self.helper(retvals, currentWord + word[pos], 0, word, pos + 1)

        # don't place char
        self.helper(retvals, currentWord, currentNum + 1, word, pos + 1)


