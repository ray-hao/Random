class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        charDict = defaultdict(lambda: 0)
        left = 0
        right = 0
        maxLen = 0
        while (right < len(s)):
            charDict[s[right]] += 1
            while len(charDict) > 2:
                charDict[s[left]] -= 1
                if charDict[s[left]] == 0:
                    del charDict[s[left]]
                left += 1
                maxLen = max(maxLen, right - left + 1)
            right += 1
            
        maxLen = max(maxLen, right - left)
        return maxLen
