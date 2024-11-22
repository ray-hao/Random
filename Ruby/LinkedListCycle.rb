# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    if not head 
        return false
    end
    
    slow = head
    fast = head.next

    while slow and fast
        if slow == fast
            return true
        end
        if not fast.next or not fast.next.next
            return false
        end
        slow = slow.next
        fast = fast.next.next
    end

    return false

end
