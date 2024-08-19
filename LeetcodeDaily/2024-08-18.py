# ok so have to either copy everything or paste everything, seems like we can start with brute force

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        seen = defaultdict(lambda: False)
        return self.backtrack(1, n, 0, 0, seen)

    def recurse(self, current, target, copied, ops, seen):
        if current + copied == target:
            return ops + 1
        elif current + copied > target:
            return float('inf')
        elif (current, copied) in seen:
            return float('inf')

        seen[(current, copied)] = True
        
        copy = self.recurse(current, target, current, ops + 1, seen)
        paste = self.recurse(current + copied, target, copied, ops + 1, seen)
        return min(copy, paste)

        
