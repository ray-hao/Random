class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charSet = set([char for char in allowed])
        retval = 0
        for word in words:
            valid = True
            for char in word:
                if char not in charSet:
                    valid = False
                    break
            if valid:
                retval += 1
                
        return retval
