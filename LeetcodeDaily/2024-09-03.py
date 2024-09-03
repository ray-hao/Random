class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intStr = ""
        for char in s:
            intStr += str(ord(char) - 96)

        for i in range(k):
            currentSum = 0
            for number in intStr:
                currentSum += int(number)
            intStr = str(currentSum)

        return int(intStr)
