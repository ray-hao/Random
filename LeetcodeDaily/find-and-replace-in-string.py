class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        indexShift = 0
        k = len(indices)

        combined = []
        for i in range(k):
            combined.append((indices[i], sources[i], targets[i]))
        
        combined.sort(key=lambda x: x[0])
        
        seen = set()

        for i in range(k):
            index = combined[i][0] + indexShift
            source = combined[i][1]
            replace = combined[i][2]
            substr = s[index: index + len(source)]
            if substr == source:
                s = s[:index] + replace + s[index + len(source):]
                indexShift += len(replace) - len(source)

        return s
