# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.goodNodeHelper_myApproach1(root, [])
        
    
    def goodNodeHelper_myApproach1(self, root, pathList):
        # This is a brute force approach, where the worst case time complexity is n^2
        #Base Case
        if root is None:
            return 0
        
        #Checking for current node
        isCurrentNodeAGoodNodeInt = 1 if self.isGoodNode( root.val, pathList ) else 0
        
        #Calling Sub problem
        pathList.append( root.val )
        leftChildAns = self.goodNodeHelper_myApproach1(root.left, pathList  )
        rightChildAns = self.goodNodeHelper_myApproach1(root.right, pathList  )
        pathList.pop()

        return isCurrentNodeAGoodNodeInt +  leftChildAns + rightChildAns
        

    def isGoodNode(self, numToCheck, numList):

        for itrNum in numList:
            if itrNum > numToCheck: 
                return False
        
        return True

# My test case of
# node_3 = TreeNode( 3 )
# node_0 = TreeNode( 0 )
# node_2 = TreeNode( 2, node_0, node_3 )
# node_1 = TreeNode(1, node_2)

# ans = Solution().goodNodes( node_1 )
# print(ans)