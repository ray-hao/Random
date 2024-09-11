class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bits = start ^ goal
        flips = 0
        while (bits > 0):
            if bits % 2 == 1:
                flips += 1
            bits = floor(bits / 2)
        return flips
