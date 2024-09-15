#
# each vowel must appear 0, 2, 4, 6, ... times.
#

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowelDict = {"a": 16, "e": 8, "i": 4, "o": 2, "u": 1}
        chars = {}
        # 1 if it's even number
        prefixes = {}
        prefixes[31] = 0
        currentMap = 31
        longest = 0
        for index, char in enumerate(s):
            if char in vowelDict:
                currentMap = currentMap ^ vowelDict[char]
            
            # if it's our first time seeing a particular bitmask, add it to the dict. If we've seen it before we want the prev index, so don't update index
            if currentMap not in prefixes:
                prefixes[currentMap] = index + 1

            # basically if we have a map at any point, we want the earliest section with the same bitmap. That means that in between this point and the earliest point, there were an even number of all vowels.
            if currentMap in prefixes:
                longest = max(longest, index + 1 - prefixes[currentMap])
        
        return longest
