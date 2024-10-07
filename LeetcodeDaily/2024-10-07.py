class Solution:
    def minLength(self, s: str) -> int:
        current = 0
        last = ""
        while last != s:
            last = s
            first = s.split("AB")
            firstStr = "".join(first)
            second = firstStr.split("CD")
            s = "".join(second)
            
        return len(s)
