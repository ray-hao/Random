class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        if (len(s) <= 1):
            return 0
        
        longests = []
        for i in range(2, len(s)):
            countDict = defaultdict(lambda: 0)
            for j in range(len(s) - i + 1):
                currentSubstr = s[j: j + i]
                countDict[currentSubstr] += 1
            maxVal = 0
            for val in countDict.values():
                maxVal = max(maxVal, val)
            longests.append(maxVal)

        for i in range(len(longests) - 1, -1, -1):
            if longests[i] != 1:
                return i + 2

        return 0
