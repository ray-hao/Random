#
# let's maintain two pointers: one for slots1 and one for slots2
#
# check overlaps using min
# check that overlaps are at least duration 
#

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        ptr1 = 0
        ptr2 = 0
        while (ptr1 < len(slots1) and ptr2 < len(slots2)):
            (start1, end1) = slots1[ptr1]
            (start2, end2) = slots2[ptr2]

            overlap = min(end1, end2) - max(start1, start2)
            if overlap >= duration:
                return [max(start1, start2), max(start1, start2) + duration]
            
            # advance one or the other
            #
            # starts and ends before other
            # starts before, ends after
            # starts after, ends before
            #
            
            if start1 <= start2 and end1 < end2:
                ptr1 += 1
            elif start2 <= start1 and end2 < end1:
                ptr2 += 1
            elif start1 <= start2 and end1 > end2:
                ptr2 += 1
            elif start2 <= start1 and end2 > end1:
                ptr1 += 1
            elif start1 >= start2 and end1 < end2:
                ptr1 += 1
            elif start2 >= start1 and end2 < end1:
                ptr2 += 1
            else:
                print(start1, end1, start2, end2)
                ptr1 += 1

        return []
