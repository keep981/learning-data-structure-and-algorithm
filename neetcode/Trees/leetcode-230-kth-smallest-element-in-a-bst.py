# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        numList = []
        self.kthSmallest_MyApproach1_InOrderTraversalListPopulator(root, numList)
        return numList[k-1]
    
    def kthSmallest_MyApproach1_InOrderTraversalListPopulator(self, root, numList):
        #I have read and checked also ki inOrderTaversal of a BST gives a sorted order of numbers
        #This approach is my first approach without thinking about the follow up that is given below
        if root is None:
            return

        self.kthSmallest_MyApproach1_InOrderTraversalListPopulator( root.left, numList )
        numList.append( root.val  )
        self.kthSmallest_MyApproach1_InOrderTraversalListPopulator( root.right, numList )