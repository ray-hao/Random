# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = head
        oddHead = head
        evenHead = head.next
        evenHeadStart = head.next
        while oddHead and evenHead:
            ogOdd = oddHead
            ogEven = evenHead
            if not evenHead.next:
                break
            oddHead = evenHead.next
            if not oddHead:
                break
            evenHead = oddHead.next
            ogOdd.next = oddHead
            ogEven.next = evenHead
        oddHead.next = evenHeadStart
        return start
