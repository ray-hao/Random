def insert_node(llist, node)

end

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
    ptr1 = list1
    ptr2 = list2
    retval = ListNode.new()
    current = retval
    while ptr1 and ptr2
        if ptr1.val <= ptr2.val
            temp = ptr1.next
            current.next = ptr1
            ptr1.next = nil
            current = ptr1
            ptr1 = temp
        else
            temp = ptr2.next
            current.next = ptr2
            ptr2.next = nil
            current = ptr2
            ptr2 = temp
        end
    end

    if ptr1
        current.next = ptr1
    else
        current.next = ptr2
    end

    return retval.next

end
