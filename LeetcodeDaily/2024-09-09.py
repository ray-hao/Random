#
# to optimize time:
#   maintain an array, and for each element in ll, append in array
#   after we know the size of the ll, we can access elements in O(1)
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodeList = []
        while head:
            nodeList.append(head)
            head = head.next

        llLength = len(nodeList)
        remainder = llLength % k
        bunch = floor(llLength / k)

        iteration = 0
        current = 0
        retval = []
        removeNexts = []
        while (iteration != k):
            iteration += 1
            if (current < len(nodeList)):
                retval.append(nodeList[current])
            else:
                retval.append(None)
            current += bunch - 1 
            if remainder > 0:
                current += 1
                remainder -= 1
            if current >= 0 and current < len(nodeList):
                removeNexts.append(nodeList[current])
            current += 1

        for remove in removeNexts:
            remove.next = None

        return retval
            
