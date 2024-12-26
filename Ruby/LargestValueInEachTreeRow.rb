# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer[]}
def largest_values(root)
    queue = Array.new
    dict = Hash.new {|h, k| h[k] = -1 * 1/0.0}

    queue.push([root, 0])
    while queue.length > 0
        poppedStuff = queue.shift
        popped, level = poppedStuff
        if not popped
            next
        end
        dict[level] = [dict[level], popped.val].max
        queue.push([popped.left, level + 1])
        queue.push([popped.right, level + 1])
    end

    retval = []
    currentLv = 0

    while dict.keys.include?(currentLv)
        retval.push(dict[currentLv])
        currentLv += 1
    end

    return retval

end
