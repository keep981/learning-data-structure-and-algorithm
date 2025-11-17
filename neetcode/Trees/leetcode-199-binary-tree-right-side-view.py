# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ansList = []
        self.rightSideViewHelper_Approach1(root, 1, ansList)
        return ansList      

    def rightSideViewHelper_Approach1(self, root, depth, ansList):
        # So the question in neetcode sheet 102. Binary Tree Level Order Traversal,  which i done previous to it helped to think this question. The solution seems like for each level of the tree the right most node present will be taken as the answert for that level. And this if you will observe our tree traversal(any one will of inorder, pre order or post order traversal, one condition left child should be called first and then right child any way the three traversal also calls the left child first and then right child, just the current node order altered) the right most node for a level will be called last. Also if you will do the dry run on the tree and see the call stack those for a level right most node will be called in the end. So solution i am thinking is we have to just update the value for a level in the ansList in each call and the order we don't have to bother, it will take care by itself.
        #Base case
        if root is None:
            return

        #Solving for current call 
        if len(ansList) < depth:
            ansList.append( root.val )
        else:
            ansList[ depth -1 ] = root.val
        
        #Calling sub problem... note here left child should be called first
        self.rightSideViewHelper_Approach1( root.left, depth + 1, ansList )
        self.rightSideViewHelper_Approach1( root.right, depth + 1, ansList )

        return

        