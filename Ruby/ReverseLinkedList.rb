# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
    if not head
        return head
    end
    
    original_node = head
    current_node = head
    next_node = head.next

    while next_node
        temp = next_node.next
        next_node.next = current_node
        current_node = next_node
        next_node = temp
    end

    original_node.next = nil
    return current_node

end
