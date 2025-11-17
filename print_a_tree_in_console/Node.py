class Node:
	def __init__(self, value, inpLeftChild = None, inpRightChild = None) -> None:
		super().__init__()
		self.value = value
		self.left = inpLeftChild
		self.right = inpRightChild
	
	def getValue(self):
		return self.value

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def setLeftChild(self, inpNode):
		self.left = inpNode

	def setRightChild(self, inpNode):
		self.right = inpNode