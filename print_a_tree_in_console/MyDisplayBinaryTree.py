
import math
from abc import ABC, abstractmethod
from Node import Node
class TreeDataInterface(ABC):
	@abstractmethod
	def getTotalNoOfLevelsInTree(self):
		pass

	@abstractmethod
	def getElementAtIdxOnCompleteBinaryTreeRepresentation(self, inpIdx):
		pass



class MyDisplayBinaryTree:
	
	@staticmethod
	def getLeftChildIdx(inpIdx):
		return (inpIdx * 2) + 1

	@staticmethod
	def getRightChildIdx(inpIdx):
		return (inpIdx * 2) + 2
	
	@staticmethod
	def getIdxPositionIn2DPrintGrid(totalLevelsInTree, elementIdx):
		
		treeLeafLevelStartingIdx = ( 1 << (totalLevelsInTree-1)  ) - 1
		if elementIdx >= treeLeafLevelStartingIdx:
			positionOfInpElementInTheLevel = elementIdx - treeLeafLevelStartingIdx
			return positionOfInpElementInTheLevel * 2
			
		leftSubProblemAns = MyDisplayBinaryTree.getIdxPositionIn2DPrintGrid(totalLevelsInTree, MyDisplayBinaryTree.getLeftChildIdx(elementIdx) )
		rightSubProblemAns = MyDisplayBinaryTree.getIdxPositionIn2DPrintGrid(totalLevelsInTree, MyDisplayBinaryTree.getRightChildIdx(elementIdx) )
		myAns =  (leftSubProblemAns + rightSubProblemAns) // 2
		return myAns


	@staticmethod
	def getNoOfLevelsInTree(noOfElementsInTree):
		return math.floor( math.log(noOfElementsInTree, 2  ) ) + 1
 
	@staticmethod
	def printCompleteBinaryTree(inpTreeDataObj: TreeDataInterface, widthToUse:int):
		
		def makeUp(inpVal:int, desiredWidth):
			return  str(inpVal).center(desiredWidth, ' ')

		def getEmptyCells(noOfCell: int , widthOfEachCell: int):
			return '-' * noOfCell * widthOfEachCell

		noOfLevelsInTree = inpTreeDataObj.getTotalNoOfLevelsInTree()
		inpListIdxItr = 0
		for lvlItr in range(1, noOfLevelsInTree + 1):
			printCursorIdxInCurrentLevel = 0
			noOfElementsInCurLvl = 1 << (lvlItr - 1)
			for _ in range(noOfElementsInCurLvl):

				idxOfCurElementInPrint2DGridRow = MyDisplayBinaryTree.getIdxPositionIn2DPrintGrid( noOfLevelsInTree, inpListIdxItr )
				print( getEmptyCells( idxOfCurElementInPrint2DGridRow - printCursorIdxInCurrentLevel, widthToUse   ), end=""  )
				print( makeUp(inpTreeDataObj.getElementAtIdxOnCompleteBinaryTreeRepresentation(inpListIdxItr) , widthToUse), end="" )
				inpListIdxItr += 1
				printCursorIdxInCurrentLevel = idxOfCurElementInPrint2DGridRow + 1
			
			print()


class TreeDataForNormalBinaryTree(TreeDataInterface):
	def __init__(self, head: Node) -> None:
		super().__init__()
		self.noOfLevel = self.computeNoOfLevelsInBinaryTree(head)
		self.idxToTreeValueInCompleteBinaryRepresntationDict = dict()
		self.initializeIdxToValueDictInCompleteBinaryTreeRepresentation(head, 0, self.idxToTreeValueInCompleteBinaryRepresntationDict)

	def computeNoOfLevelsInBinaryTree(self, inpNode: Node) -> int:
		if inpNode is None:
			return 0
		return 1 + max( self.computeNoOfLevelsInBinaryTree(inpNode.getLeftChild()), self.computeNoOfLevelsInBinaryTree(inpNode.getRightChild()) )

	def initializeIdxToValueDictInCompleteBinaryTreeRepresentation(self, inpNode: Node, curInpNodeIdx: int , dictToPopulate):
		if inpNode is None:
			return

		dictToPopulate[curInpNodeIdx] = inpNode.getValue()
		self.initializeIdxToValueDictInCompleteBinaryTreeRepresentation( inpNode.getLeftChild(), curInpNodeIdx * 2 + 1, dictToPopulate  )
		self.initializeIdxToValueDictInCompleteBinaryTreeRepresentation( inpNode.getRightChild(), curInpNodeIdx * 2 + 2, dictToPopulate  )

	def getTotalNoOfLevelsInTree(self):
		return self.noOfLevel
	
	def getElementAtIdxOnCompleteBinaryTreeRepresentation(self, inpIdx ):
		return self.idxToTreeValueInCompleteBinaryRepresntationDict.get( inpIdx, None )


class TreeDataForCompleteBinaryTree(TreeDataInterface):
	def __init__(self, completeBinaryTreeListRepresentation: list[int]) -> None:
		super().__init__()
		self.completeBinaryTreeListRepresentation = completeBinaryTreeListRepresentation
		self.noOfLevel = math.floor( math.log(len(completeBinaryTreeListRepresentation), 2 ) ) + 1

	def getTotalNoOfLevelsInTree(self):
		return self.noOfLevel
	
	def getElementAtIdxOnCompleteBinaryTreeRepresentation(self, inpIdx ):
		# As we are naming it as complete binary tree, the caller might call for a index on the last level but it is not present in our data yet, for that we will be returning None for now
		if inpIdx >= len(self.completeBinaryTreeListRepresentation):
			return None
		return self.completeBinaryTreeListRepresentation[inpIdx]



if __name__ == "__main__":
	nodeF = Node(15)
	nodeG = Node(993)
	nodeC =  Node(761, nodeF, nodeG)
	nodeB = Node(34)
	nodeA = Node(272, nodeB, nodeC)

	treeDataForNormalBinaryTree = TreeDataForNormalBinaryTree(nodeA)
	print( treeDataForNormalBinaryTree.getTotalNoOfLevelsInTree() )
	print( treeDataForNormalBinaryTree.getElementAtIdxOnCompleteBinaryTreeRepresentation(5) )

	MyDisplayBinaryTree.printCompleteBinaryTree(treeDataForNormalBinaryTree,9)

	print("*********************************Separator*********************************")
	# Another one
	MyDisplayBinaryTree.printCompleteBinaryTree(  TreeDataForCompleteBinaryTree([24,657,24,136,35,892,1234,741,2134]), 9 )



		