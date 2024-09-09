#
# given points on x-y plane
#
# add new points to data structure, duplicate points allowed
# given a point, basically need to keep track of all points with same x or y values
#


class DetectSquares:

    def __init__(self):
        self.xPoints = defaultdict(lambda: [])
        self.yPoints = defaultdict(lambda: [])
        self.points = defaultdict(lambda: 0)
        

    def add(self, point: List[int]) -> None:
        [x, y] = point
        self.xPoints[x].append(point)
        self.yPoints[y].append(point)
        self.points[(x, y)] += 1
        
    def count(self, point: List[int]) -> int:
        num = 0
        [x, y] = point

        # when we choose 3 other points, we need 1 to be the same x or y axis as the current point. We also need 2 other points to be axis parallel on the same axis as the the current point and 1 other.

        for sameXPoint in self.xPoints[x]:
            sideLength = abs(y - sameXPoint[1])
            if sideLength != 0:
                if (x + sideLength, y) in self.points and (sameXPoint[0] + sideLength, sameXPoint[1]) in self.points:
                    num += self.points[(x + sideLength, y)] * self.points[(sameXPoint[0] + sideLength, sameXPoint[1])]
                if (x - sideLength, y) in self.points and (sameXPoint[0] - sideLength, sameXPoint[1]) in self.points:
                    num += self.points[(x - sideLength, y)] * self.points[(sameXPoint[0] - sideLength, sameXPoint[1])]

        return num

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
