# My brute force approach surprisingly accepted by leetcode. Although it was in the bottom percentile in the speed only beating 5% of Users.
# In my brute force approach i also did not used the binary search tree feature at all.
# To read other's solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    class PQPresentCarrier:
        def __init__(self, isPPresent, isQPresent ):
            self.isPPresent = isPPresent
            self.isQPresent = isQPresent

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lowestCommonAncestor_MyApproach1_BruteForce( root, p, q )

    def lowestCommonAncestor_MyApproach1_BruteForce(self, root, p, q):
        #We will do a post order traversal and for each node we will call another function for checking if both p and q exist within that node's subtree(including that node also). By doing post order traversal we will give the Lowest Common Ancestor to match first. And once we get a match we will bubble that up till the top and that will be the answer
        # In this approach We will save calls that falls after Lowest Common Ancestor in post order traversal
        
        #Base Case
        #Basically the return type of this function will be a TreeNode, so for base case that is when root is None then we will return None
        if root is None:
            return None

        #Sub Problem
        leftAns = self.lowestCommonAncestor_MyApproach1_BruteForce( root.left, p, q )
        if leftAns is not None:
            return leftAns
            
        rightAns = self.lowestCommonAncestor_MyApproach1_BruteForce( root.right, p, q )
        if rightAns is not None:
            return rightAns

        #Solving for current node
        pqPresentCarrierObj = self.bothNodeExitsInSubtree( root, p, q )
        if pqPresentCarrierObj.isPPresent and pqPresentCarrierObj.isQPresent:
            return root #This is the lowest common ancestor, we will reach this line once in the code run. For the calls to the nodes above to it we will return from the above checks. 
        else:
            return None
    
    def bothNodeExitsInSubtree(self, subTreeRoot, p, q):
        #I think we need to do values comparison.
        #Base Case  
        if subTreeRoot is None:
            return self.PQPresentCarrier(False, False)
        
        #Sub Problem
        pqPresentCarrierObjLeft = self.bothNodeExitsInSubtree( subTreeRoot.left, p, q  )
        pqPresentCarrierObjRight = self.bothNodeExitsInSubtree( subTreeRoot.right, p, q  )

        isCurrentRootSameAsP = subTreeRoot.val == p.val
        isCurrentRootSameAsQ = subTreeRoot.val == q.val

        return self.PQPresentCarrier( 
            pqPresentCarrierObjLeft.isPPresent or pqPresentCarrierObjRight.isPPresent or isCurrentRootSameAsP
            , pqPresentCarrierObjLeft.isQPresent or pqPresentCarrierObjRight.isQPresent or isCurrentRootSameAsQ
         )