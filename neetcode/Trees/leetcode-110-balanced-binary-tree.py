# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    class InfoCarrier:
        def __init__(self, height, isHeightBalancedIncludingDescedants):
            self.height = height
            self.isHeightBalancedIncludingDescedants = isHeightBalancedIncludingDescedants

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        self.isBalancedHelper_myApproach1(root).isHeightBalancedIncludingDescedants

    def isBalancedHelper_myApproach1(self, root):
        #So we have to check the height at each node and if any node is failing then that we should sending bubble up till the root node.
        #Base Case
        if root is None:
            return self.InfoCarrier(0, True)

        #Sub problem
        infoCarObjLeft = self.isBalancedHelper_myApproach1( root.left )
        infoCarObjRight = self.isBalancedHelper_myApproach1( root.right )

        #CurrentNode calculation
        curretNodeHieghtBalancedAns = (
            ( abs(infoCarObjLeft.height - infoCarObjRight.height) <= 1  )
            and infoCarObjLeft.isHeightBalancedIncludingDescedants
            and infoCarObjRight.isHeightBalancedIncludingDescedants
        )
        
        print(f"Ans at node{root.val}={curretNodeHieghtBalancedAns}")

        return self.InfoCarrier(max(infoCarObjLeft.height, infoCarObjRight.height) + 1, curretNodeHieghtBalancedAns)


        