# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        ptr1 = poly1
        ptr2 = poly2

        retval = PolyNode()
        current = retval

        while (ptr1 or ptr2):
            if (ptr1 and ptr2):
                if (ptr1.power == ptr2.power):
                    if ptr1.coefficient + ptr2.coefficient == 0:
                        ptr1 = ptr1.next
                        ptr2 = ptr2.next
                    else:
                        current.next = PolyNode(ptr1.coefficient + ptr2.coefficient, ptr1.power, None)
                        current = current.next
                        ptr1 = ptr1.next
                        ptr2 = ptr2.next
                elif (ptr1.power > ptr2.power):
                    current.next = PolyNode(ptr1.coefficient, ptr1.power, None)
                    current = current.next
                    ptr1 = ptr1.next
                else:
                    current.next = PolyNode(ptr2.coefficient, ptr2.power, None)
                    current = current.next
                    ptr2 = ptr2.next
            elif (ptr1 and not ptr2):
                current.next = PolyNode(ptr1.coefficient, ptr1.power, None)
                current = current.next
                ptr1 = ptr1.next
            else:
                current.next = PolyNode(ptr2.coefficient, ptr2.power, None)
                current = current.next
                ptr2 = ptr2.next

        return retval.next



    
