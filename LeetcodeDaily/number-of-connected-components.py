class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def add(self, first, second):

        if self.parent[first] == self.parent[second]:
            return

        while self.parent[first] != first:
            first = self.parent[first]
        
        while (self.parent[second] != second):
            second = self.parent[second]

        if first != second:
            self.parent[second] = self.parent[first]

        return

    def getSets(self):
        seen = set()
        for s in self.parent:
            if self.parent[s] == s:
                seen.add(s)
        
        return len(seen)
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        sets = DisjointSet(n)

        for edge in edges:
            [v1, v2] = edge
            sets.add(v1, v2)

        return sets.getSets()
        
