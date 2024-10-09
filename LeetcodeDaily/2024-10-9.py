#
# basically, count the number of extraneous open or close 
#
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(bracket)
        
        return len(stack)
      
