#
# ok let's just consider the increasing teams case W.L.O.G. 
#
# let's say we look at all of the soldiers one by one and we're at index i right now. We want to figure out how many teams include soldier i as the third member
#   - we only need to look at the soldiers before soldier i
#   - we need soldier i to be before soldier j, who is in line before soldier i
#   - if soldier i is bigger than soldier j, and soldier j is bigger than k soldiers, then any of the k soldiers can be first, soldier j can be second, and soldier i can be third. 
#       - we're basically fixing the third and second soldier to ensure there aren't any duplicates.
#

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        idp = [0] * len(rating)
        iTeams = 0

        ddp = [0] * len(rating)
        dTeams = 0

        for i in range(len(rating)):
            for j in range(i):
                if rating[i] > rating[j]:
                    idp[i] += 1
                    iTeams += idp[j]
                if rating[i] < rating[j]:
                    ddp[i] += 1
                    dTeams += ddp[j]

        return iTeams + dTeams
      
