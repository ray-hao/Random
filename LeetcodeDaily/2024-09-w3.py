#
# we can represent this as a tree problem, LCA
#

class TreeNode:
    def __init__(self, region = "", children = []):
        self.region = region
        self.children = children

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        # ok so basically we just model this as an n-ary tree, and we need to get
        # 'root' node. This node will appear as a parent but never a child.
        regionMap = {}
        parentList = set()
        childrenList = set()
        for region in regions:
            parentRegion = region[0]
            parentList.add(parentRegion)
            if parentRegion not in regionMap:
                regionMap[parentRegion] = set()
            for childRegionIndex in range(1, len(region)):
                childRegion = region[childRegionIndex]
                childrenList.add(childRegion)
                if childRegion not in regionMap[parentRegion]:
                    regionMap[parentRegion].add(childRegion)

        # root node, to call self.LCAhelper from
        largestRegion = [x for x in parentList if x not in childrenList][0]

        # now get LCA
        LCA = self.LCAHelper(regionMap, region1, region2, largestRegion)
        return LCA
    
    # helper to get LCA
    def LCAHelper(self, regionMap, target1, target2, current):
        print(current)
        if current == target1 or current == target2:
            return current
        
        if current not in regionMap:
            return None

        values = []
        for childRegion in regionMap[current]:
            retval = self.LCAHelper(regionMap, target1, target2, childRegion)
            if retval:
                values.append(retval)
        # if there's only one value, then it's the LCA
        # if there are multiple values, then the current node is LCA
        processValues = set(values)
        if len(processValues) == 1:
            return values[0]
        elif len(processValues) == 2:
            return current


        
        
