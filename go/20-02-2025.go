/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// We want to recover the same structured tree, but with correct values
// So we need to maintain the root (and it will point to all children and stuff)
// For faster lookup in find() we can also have a map
type FindElements struct {
    Root *TreeNode
    Seen map[int]bool
}


func Constructor(root *TreeNode) FindElements {
    treeNodeList := []*TreeNode{}
    root.Val = 0
    treeNodeList = append(treeNodeList, root)
    seenDict := make(map[int]bool)
    for len(treeNodeList) > 0 {
        // include : exclude 
        currentNode := treeNodeList[len(treeNodeList) - 1 :][0]
        if currentNode == nil {
            break
        } 
        treeNodeList = treeNodeList[: len(treeNodeList) - 1]
        currentVal := currentNode.Val
        seenDict[currentVal] = true
        if currentNode.Left != nil {
            currentNode.Left.Val = currentVal * 2 + 1
            treeNodeList = append(treeNodeList, currentNode.Left)
        }
        if currentNode.Right != nil {
            currentNode.Right.Val = currentVal * 2 + 2
            treeNodeList = append(treeNodeList, currentNode.Right)
        }
    }
    recoveredTree := FindElements{Root: root, Seen: seenDict}
    return recoveredTree
}


func (this *FindElements) Find(target int) bool {
    _, ok := this.Seen[target]
    return ok
}


/**
 * Your FindElements object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Find(target);
 */
