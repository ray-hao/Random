# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #
    # ITERATIVE SOLUTION
    #

    #
    # we want to handle left, then current, then right
    #

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trav = []
        seen = set()
        stack = []
        stack.append(root)
        while (len(stack) > 0):
            currentNode = stack.pop()
            if not currentNode:
                continue

            if currentNode.left and currentNode.left not in seen:
                stack.append(currentNode)
                stack.append(currentNode.left)
                continue
            if currentNode.right and currentNode.right not in seen:
                stack.append(currentNode)
                stack.append(currentNode.right)
                continue
            trav.append(currentNode.val)
            seen.add(currentNode)
            
        print(trav)
        return trav



    #
    # RECURSIVE SOLUTION
    #

    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    #     if not root:
    #         return []

    #     if not root.left and not root.right:
    #         return [root.val]

    #     vals = []
    #     self.helper(root, vals)
    #     return vals

    # def helper(self, node, vals):
    #     if not node:
    #         return

    #     if not node.left and not node.right:
    #         vals.append(node.val)
    #         return
        
    #     self.helper(node.left, vals)
    #     self.helper(node.right, vals)
    #     vals.append(node.val)
