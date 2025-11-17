# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ansList = []
        self.levelOrderHelper( root, 1, ansList )
        return ansList
    
    def levelOrderHelper(self, root, depth, ansList):
        # Here we are top to down addition to the list. Will be appending to thr ansList passed to a call. For the next level we will call them with one depth added
        if root is None:
            return
        
        #Will solve for current problem 
        if len(ansList) < depth:
            ansList.append( [root.val] )
        else:
            ansList[ depth - 1 ].append( root.val  )

        #Call sub problems
        self.levelOrderHelper( root.left, depth + 1, ansList )
        self.levelOrderHelper( root.right, depth + 1, ansList )

        return