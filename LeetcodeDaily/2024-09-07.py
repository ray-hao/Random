# put all nums in a set for O(1) access
# use fast pointer and slow pointer - if fast pointer is in set 
# then set the slow pointer to next element not in set.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        delete = set()
        for num in nums:
            delete.add(num)

        if not head:
            return head

        initial = head

        slow = head
        fast = head.next
        deleting = False
        while fast:
            if fast.val in delete:
                deleting = True
                fast = fast.next
            else:
                if deleting:
                    slow.next = fast
                    deleting = False
                slow = fast
                fast = fast.next
        if deleting:
            slow.next = None
        if initial.val in delete:
            return initial.next

        return initial
