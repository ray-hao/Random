type Pair struct {
    Level int
    Val int
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func recoverFromPreorder(traversal string) *TreeNode {
    // keep track of which TreeNode we should be addding children to

    nodeStack := make([]Pair, 0, 0)
    currentLevel := 0
    currentStrPos := 0
    for {
        if currentStrPos >= len(traversal) {
            break
        } else if traversal[currentStrPos] == '-' {
            currentLevel += 1
            currentStrPos += 1
        } else {
            startIdx := currentStrPos
            for {
                if currentStrPos >= len(traversal) || traversal[currentStrPos] == '-' {
                    var val int
                    if currentStrPos >= len(traversal) {                    
                        val, _ = strconv.Atoi(traversal[startIdx : ])
                    } else {
                        val, _ = strconv.Atoi(traversal[startIdx : currentStrPos])
                    }
                    nodeStack = append(nodeStack, Pair{Level: currentLevel, Val: val})
                    currentLevel = 0
                    break
                }
                currentStrPos += 1
            }
        }
    }

    nodeMap := make(map[int]*TreeNode)

    for len(nodeStack) > 0 {
        popped := nodeStack[0]
        level := popped.Level
        val := popped.Val

        newNode := &TreeNode{ Val: val, Left: nil, Right: nil }

        if level == 0 {
            nodeMap[0] = newNode
        } else {
            parent := nodeMap[level - 1]
            if parent.Left == nil {
                parent.Left = newNode
            } else {
                parent.Right = newNode
            }
            nodeMap[level] = newNode
        }

        nodeStack = nodeStack[1:]
    }

    return nodeMap[0]
}
