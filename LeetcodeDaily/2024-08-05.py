class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        items = {}
        for item in arr:
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
        distincts = []
        for item in arr:
            if items[item] == 1:
                distincts.append(item)

        if len(distincts) >= k:
            return distincts[k - 1]
        return ""
