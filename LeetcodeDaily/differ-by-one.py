class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        lengthDict = defaultdict(lambda: [])
        for item in dict:
            lengthDict[len(item)].append(item)

        for items in lengthDict.items():
            (key, val) = items
            for i in range(1, key + 1):
                seen = set()
                for string in val:
                    current = string[:i - 1] + string[i:]
                    if current in seen:
                        print(current, seen)
                        return True
                    seen.add(current)

        return False
