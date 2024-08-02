class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = [deet[11:13] for deet in details]
        count = 0
        for age in ages:
            if int(age) > 60:
                count += 1
        return count
        
