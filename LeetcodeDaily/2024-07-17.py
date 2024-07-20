# to delete a node, we need to get rid of the parent's pointer to the deletee
# and to remove the deletee's pointers to its children

# we should delete the lowest nodes first. each time we delete a node, we should add its children
# to an array storing roots of the forest. also when we are considering a node, we should 
# delete its links to any children that should be deleted.

# This is exactly postorder traversal!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        roots = []
        self.postorder(root, roots, to_delete)
        if root.val not in to_delete:
            roots.append(root)
        return roots

    def postorder(self, root, forestRoots, to_delete):
        if root.left:
            self.postorder(root.left, forestRoots, to_delete)
        if root.right:
            self.postorder(root.right, forestRoots, to_delete)
        if root.val in to_delete:
            if root.right and root.right.val not in to_delete:
                forestRoots.append(root.right)
            if root.left and root.left.val not in to_delete:
                forestRoots.append(root.left)
        if root.right and root.right.val in to_delete:
            root.right = None
        if root.left and root.left.val in to_delete:
            root.left = None
        
