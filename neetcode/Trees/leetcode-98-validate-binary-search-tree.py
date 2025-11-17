# ************************************************************* #

# In first solution, i take this solution very casually and take it for granted without thinking of possible cases. And created the wrong solution mentioned in function isValidBST_MyFirstWrongSolution. I did not paid attention what it is mentioned in the description also. It is clearly mentioned ki in a BST, `The left subtree of a node contains only nodes with keys less than the node's key and The right subtree of a node contains only nodes with keys greater than the node's key.`. Here the subtree thing i did not taken into consideratin. I was just checking ki each nodes is and it's left and right child should be smaller and greater respectively. But rather we should be checking the whole subtree. So failed for the testcase one  example is [5, 1, 6, null, null, 3, 7]. as per the leetcode style i have written. You can build the tree diagram accordingly. 

# ************************************************************* #


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST_MyFirstWrongSolution(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        isCurrentNodeLeftChildSatisfyBstRule =  (root.left is None) or ( root.val > root.left.val )
        isCurrentNodeRightChildSatisfyBstRule = (root.right is None) or ( root.val < root.right.val )
        
        if isCurrentNodeLeftChildSatisfyBstRule and isCurrentNodeRightChildSatisfyBstRule:
            return self.isValidBST(root.left) and self.isValidBST(root.right)

        else:
            return False
        


    def isValidBSTHelper(self, root):
        #This function can not handle if the root is none itself, so in the calling function we have to handle this case

        if root.left is None and root.right is None:
            #Making this node as base case as it avoid initializing minValInSubTree, maxValInSubTree with INT_MIN and INT_MAX
            isGreenSignalForCurrentNode = True
            newSubTreeMin = root.val
            newSubTreeMax = root.val

        elif root.left is None:
            rightChildAns = self.isValidBSTHelper( root.right )
            isGreenSignalForCurrentNode = rightChildAns.isBST and (rightChildAns.minValInSubTree > root.val )
            newSubTreeMin = min( root.val, rightChildAns.minValInSubTree )
            newSubTreeMax = max( root.val, rightChildAns.maxValInSubTree )
        
        elif root.right is None:
            leftChildAns = self.isValidBSTHelper( root.left )
            isGreenSignalForCurrentNode = leftChildAns.isBST and (leftChildAns.maxValInSubTree < root.val )
            newSubTreeMin = min( root.val, leftChildAns.minValInSubTree )
            newSubTreeMax = max( root.val, leftChildAns.maxValInSubTree )
        else:
            leftChildAns = self.isValidBSTHelper( root.left )
            rightChildAns = self.isValidBSTHelper( root.right )
            isGreenSignalForCurrentNode = leftChildAns.isBST and rightChildAns.isBST and (leftChildAns.maxValInSubTree < root.val )and (rightChildAns.minValInSubTree > root.val )
            newSubTreeMin = min( root.val, leftChildAns.minValInSubTree, rightChildAns.minValInSubTree )
            newSubTreeMax = max( root.val, leftChildAns.maxValInSubTree, rightChildAns.maxValInSubTree )

        
        return self.InfoCarrier( isGreenSignalForCurrentNode, newSubTreeMin, newSubTreeMax   )