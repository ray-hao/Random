#
# appears once in one sentence and not in the other
#

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        myDict = defaultdict(lambda: 0)
        s1Words = s1.split(" ")
        s2Words = s2.split(" ")
        for word in s1Words + s2Words:
            myDict[word] += 1
        
        retvals = []
        for key, val in myDict.items():
            if val == 1:
                retvals.append(key)

        return retvals
