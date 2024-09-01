class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        retval = []
        for i in range(m):
            current = original[i * n : i * n + n]
            retval.append(current)


        return retval
