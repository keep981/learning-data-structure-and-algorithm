from MyDisplayBinaryTree import MyDisplayBinaryTree, TreeDataForCompleteBinaryTree

class MinHeap:
	def __init__(self):
		self.container = list()
		
	@staticmethod
	def initFromAList(inpList: list[int]):
		minHeapObj = MinHeap()
		for itm in inpList:
			minHeapObj.insert(itm)
		return minHeapObj
		
	@staticmethod
	def getParentNodeIdx(inpIdx):
		return (inpIdx - 1) // 2
	
	@staticmethod
	def getLeftChildIdx(inpIdx):
		return (inpIdx * 2) + 1
		
	@staticmethod
	def getRightChildIdx(inpIdx):
		return (inpIdx * 2) + 2
	
	def getContainer(self):
		return self.container

	def swapElementsAtIndices(self, idxOne, idxTwo):
		temp = self.container[idxOne]
		self.container[idxOne] = self.container[idxTwo]
		self.container[idxTwo] = temp

	def checkAndResolveHeapPropertyAboveTheLadder(self, inpIdx):
		idxItr = inpIdx
		isLadderFixed = False
		while(not isLadderFixed):
			parentIdx = MinHeap.getParentNodeIdx(idxItr)
			if (idxItr == 0) or ( self.container[parentIdx] <= self.container[idxItr] ):
				isLadderFixed = True
				continue

			self.swapElementsAtIndices(  idxItr, parentIdx )
			idxItr = parentIdx

	def insert(self, newVal: int):
		self.container.append(newVal)
		self.checkAndResolveHeapPropertyAboveTheLadder( len(self.container) - 1 )


	def heapify(self, violatedIdx:int):
		noOfElementsInTree = len(self.container)

		idxItr = violatedIdx

		# while (idxItr < noOfElementsInTree):

		





originalList = [923,657,611,892,1234,35,741,89, 136,2134]
minHeapObj = MinHeap.initFromAList(originalList)

MyDisplayBinaryTree.printCompleteBinaryTree(  TreeDataForCompleteBinaryTree(originalList), 5)
print("************************************Separator************************************")
MyDisplayBinaryTree.printCompleteBinaryTree(  TreeDataForCompleteBinaryTree(minHeapObj.getContainer()), 5)
