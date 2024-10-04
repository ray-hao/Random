class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        numTeams = int(len(skill) / 2)
        sum = 0
        for s in skill:
            sum += s
        
        if sum % numTeams != 0:
            return -1

        target = int(sum / numTeams)
        pairs = []
        playerDict = defaultdict(lambda : [])
        for index, s in enumerate(skill):
            if s > target:
                return -1
            if target - s in playerDict:
                teammate = playerDict[target - s].pop(0)
                if len(playerDict[target - s]) == 0:
                    del playerDict[target - s]
                pairs.append((s, skill[teammate]))
            else:
                playerDict[s].append(index)

        if len(pairs) != len(skill) / 2:
            return -1

        chemistry = 0
        for pair in pairs:
            chemistry += pair[0] * pair[1]

        return chemistry

        
