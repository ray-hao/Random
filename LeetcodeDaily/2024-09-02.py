#
# Easy solution is to continuously loop through the students, subtracting 
# chalk[i] at each step.
#


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        sum = 0
        for piece in chalk:
            sum += piece

        k = k % sum

        current = 0
        while True:
            if k < chalk[current]:
                return current
            else:
                k -= chalk[current]
                if (current == len(chalk) - 1):
                    current = 0
                else:
                    current += 1
    
