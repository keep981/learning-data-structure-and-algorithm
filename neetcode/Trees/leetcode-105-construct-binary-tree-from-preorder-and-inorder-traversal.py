# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    class TreeNode(object):
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if preorder[0] is None:
            return None

        return self.buildTreeHelper_myApproach1( preorder, inorder, 0, 0, len(preorder) -1  )
        
    def buildTreeHelper_myApproach1(self, preorder, inorder, preOrderStartIdx, inOrderStartIdx, inOrderEndIdx ):

        #Approach is first we will create a node at the preorder[ preOrderStartIdx ]
        #Then we will find that value in inorder array. To the left of that node value in inorder array, they will go to the left subtree. And after that will go to the right subtree

        #Base case we have reached an end node of the tree, other words this call is made from an leaf node
        if inOrderStartIdx > inOrderEndIdx:
            return None
        
        elementToCreateNodeAtThisCall = preorder[ preOrderStartIdx ]
        elementIdxInInorderList = self.findIndexOfElemInList( inorder, inOrderStartIdx, inOrderEndIdx, elementToCreateNodeAtThisCall  )
        noOfElementsInLeftSubTree = elementIdxInInorderList - inOrderStartIdx

        leftSubTree = self.buildTreeHelper_myApproach1( preorder, inorder, preOrderStartIdx + 1, inOrderStartIdx, elementIdxInInorderList - 1   )
        
        rightSubTree_preOrderStartIdx = preOrderStartIdx + noOfElementsInLeftSubTree + 1 #Think deep
        rightSubTree = self.buildTreeHelper_myApproach1( preorder, inorder, rightSubTree_preOrderStartIdx, elementIdxInInorderList + 1, inOrderEndIdx   )

        currentNode = self.TreeNode( elementToCreateNodeAtThisCall, leftSubTree, rightSubTree )
        return currentNode

    def findIndexOfElemInList( self, inpList, startIdx, endIdx, elemToFind ):
        for itrIdx in range(startIdx, endIdx):
            if inpList[ itrIdx ] == elemToFind:
                return itrIdx
        
        #Did not get the element, halaki ei jau example re mu code karuchi ethiki asiba katha nuha
        return -1
    




ans = Solution().buildTree( [3,9,20,15,7], [9,3,15,20,7] )
