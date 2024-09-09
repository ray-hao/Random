# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1] * n for _ in range(m)]
        row = 0
        col = 0
        # 0 is right, 1 is down, 2 is left, 3 is up
        direction = 0

        topBound = 1
        bottomBound = m - 1
        rightBound = n - 1
        leftBound = 0

        while head:
            matrix[row][col] = head.val
            if direction == 0:
                if col < rightBound:
                    col += 1
                else:
                    direction = 1
                    rightBound -= 1
                    row += 1
            elif direction == 1:
                if row < bottomBound:
                    row += 1
                else:
                    direction = 2
                    bottomBound -= 1
                    col -= 1
            elif direction == 2:
                if col > leftBound:
                    col -= 1
                else:
                    direction = 3
                    leftBound += 1
                    row -= 1
            else:
                if row > topBound:
                    row -= 1
                else:
                    direction = 0
                    topBound += 1
                    col += 1
            head = head.next
            
        return matrix
