# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
    if root == nil
        return nil
    elsif root == p
        return p
    elsif root == q
        return q
    else
        leftAns = lowest_common_ancestor(root.left, p, q)
        rightAns = lowest_common_ancestor(root.right, p, q)
        if (not leftAns) and rightAns
            return rightAns
        elsif (not rightAns) and leftAns
            return leftAns
        elsif rightAns and leftAns
            return root
        else
            return nil
        end
    end
end
