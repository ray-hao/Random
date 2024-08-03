class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        first = sorted(target)
        second = sorted(arr)
        return first == second
        
