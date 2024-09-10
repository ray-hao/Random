#
# basically find GCD, insert in between each pair of adjacent nodes
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original = head
        current = head
        next = head.next

        while True:
            if current and next:
                factors1 = self.factorize(current.val)
                factors2 = self.factorize(next.val)
                gcd = self.getGCD(factors1, factors2)
                newNode = ListNode(gcd)
                current.next = newNode
                newNode.next = next
                current = next
                next = next.next
            else:
                break
        return original
        
    def factorize(self, num):
        if num == 1:
            return {1: 1}
        
        factors = defaultdict(lambda: 0)

        while (num != 1):
            if num % 2 == 0:
                factors[2] += 1
                num /= 2
            else: 
                for i in range(3, int(num) + 1, 2):
                    if (num % i == 0):
                        factors[i] += 1
                        num /= i
                        break

        return factors

    def getGCD(self, factors1, factors2):
        gcd = 1
        for key in factors1.keys():
            if key in factors2.keys():
                print(min(factors1[key], factors2[key]))
                gcd *= key**min(factors1[key], factors2[key])

        return gcd
