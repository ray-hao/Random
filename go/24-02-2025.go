type RayTreeNode struct {
    Neighbors []*RayTreeNode
    Value     int
    Number    int
}

func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    // bob's path is already determined, he will move up one at a time
    // we know the timestamps too that bob will reach each node
    // we want a full exploration, keeping track of times (to take bob into account)
    nodeMap := make(map[int]*RayTreeNode)
    for _, edge := range edges {
        firstNode, secondNode := edge[0], edge[1]
        _, ok := nodeMap[firstNode]
        if !ok {
            newNode := &RayTreeNode{}
            newNode.Number = firstNode
            nodeMap[firstNode] = newNode
        }
        
        _, ok = nodeMap[secondNode]
        if !ok {
            newNode := &RayTreeNode{}
            newNode.Number = secondNode
            nodeMap[secondNode] = newNode
        }

        nodeMap[firstNode].Neighbors = append(nodeMap[firstNode].Neighbors, nodeMap[secondNode])
        nodeMap[secondNode].Neighbors = append(nodeMap[secondNode].Neighbors, nodeMap[firstNode])
    }

    for index, value := range amount {
        nodeMap[index].Value = value
    }

    // node => time he was there 
    bobPath := make(map[int]int)
    DFS(bobPath, bob, 0, make(map[int]bool), nodeMap)    
    return AliceDfs(0, make(map[int]bool), bobPath, 0, nodeMap)
}

func DFS(path map[int]int, currentNode int, currentStep int, visited map[int]bool, nodeMap map[int]*RayTreeNode) bool {

    if currentNode == 0 {
        path[currentNode] = currentStep
        return true
    }

    options := nodeMap[currentNode].Neighbors
    visited[currentNode] = true
    path[currentNode] = currentStep
    for _, option := range options {
        _, seen := visited[option.Number]
        if seen {
            continue
        } else {
            valid := DFS(path, option.Number, currentStep + 1, visited, nodeMap)
            if valid {
                return true
            }
        }
    }
    delete(visited, currentNode)
    delete(path, currentNode)
    return false

}

func AliceDfs(currentNode int, visited map[int]bool, bobPath map[int]int, currentStep int, nodeMap map[int]*RayTreeNode) int {

    currentValue := 0
    timeStamp, bobSeen := bobPath[currentNode]
    if bobSeen {
        if timeStamp == currentStep {
            currentValue = nodeMap[currentNode].Value / 2
        } else if timeStamp > currentStep {
            currentValue = nodeMap[currentNode].Value
        }
    } else {
        currentValue = nodeMap[currentNode].Value
    }

    if len(nodeMap[currentNode].Neighbors) == 1 {
        if _, ok := visited[nodeMap[currentNode].Neighbors[0].Number]; ok {
            return currentValue
        }
    }

    visited[currentNode] = true
    options := nodeMap[currentNode].Neighbors
    retval := -9999999999999999
    for _, option := range options {
        _, seen := visited[option.Number]
        if seen {
            continue
        }
        optionVal := AliceDfs(option.Number, visited, bobPath, currentStep + 1, nodeMap)
        if optionVal > retval {
            retval = optionVal
        }
    }
    delete(visited, currentNode)
    return retval + currentValue

}

