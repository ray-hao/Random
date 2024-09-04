class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacleDict = {}
        for obstacle in obstacles:
            [x, y] = obstacle
            obstacleDict[(x, y)] = True
        maxDist = 0
        currentPos = (0, 0)
        # 1 is north, 2 is east, 3 is south, 4 is west
        direction = 1
        for command in commands:
            if command == -2:
                if direction == 1:
                    direction = 4
                else:
                    direction -= 1
            elif command == -1:
                if direction == 4:
                    direction = 1
                else:
                    direction += 1
            else:
                # check boundaries, obstacles
                if direction == 1:
                    for i in range(command):
                        if ((currentPos[0], currentPos[1] + 1) in obstacleDict):
                            break
                        currentPos = (currentPos[0], currentPos[1] + 1)
                elif direction == 2:
                    for i in range(command):
                        if ((currentPos[0] + 1, currentPos[1]) in obstacleDict):
                            break
                        currentPos = (currentPos[0] + 1, currentPos[1])
                elif direction == 3:
                    for i in range(command):
                        if ((currentPos[0], currentPos[1] - 1) in obstacleDict):
                            break
                        currentPos = (currentPos[0], currentPos[1] - 1)
                else:
                    for i in range(command):
                        if ((currentPos[0] - 1, currentPos[1]) in obstacleDict):
                            break
                        currentPos = (currentPos[0] - 1, currentPos[1])

            maxDist = max(maxDist, currentPos[0] ** 2 + currentPos[1] ** 2)


        return maxDist
