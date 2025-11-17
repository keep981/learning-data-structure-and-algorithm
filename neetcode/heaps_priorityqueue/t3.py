#This is the leetcode compiler version, without they data type hints
class MyMinHeap(object):
    def __init__(self):
        self.data = []
    
    @classmethod
    def buildMinHeapFromList(cls, inpList):
        mmh = cls()
        for item in inpList:
            mmh.insert( item )
        return mmh
    
    def size(self):
        return len(self.data)
    
    def getParentIndex(self, idx):
        return (idx - 1) // 2
    
    def getLeftChildIndex(self, idx):
        return idx * 2 + 1
    
    def getRightChildIndex(self, idx):
        return idx * 2 + 2    

    def swapTwoIndexValues(self, id1, id2 ):
        tempContainer = self.data[id1]
        self.data[id1] = self.data[id2]
        self.data[id2] = tempContainer

    def insert(self, element):
        # Will add the element to the end of the list, so it will satisfy the complete binary tree property.
        # But the heap min property might get violated in it's parent (also in ancestor) nodes. So we will recursively check upwards.
        self.data.append(element) 
        itrElemIdx = len(self.data) - 1
        while True:
            parentIdxOfItrElement = self.getParentIndex( itrElemIdx )
            if (parentIdxOfItrElement < 0) or ( self.data[itrElemIdx] > self.data[parentIdxOfItrElement] ):
                break
            else:
                #swap the two values
                self.swapTwoIndexValues( itrElemIdx, parentIdxOfItrElement )
                itrElemIdx = parentIdxOfItrElement
                continue
    
    def heapify(self, index):
        #The min heap property is violated at the given index, so we will take the minimum out of the given index and it's left and right child.
        # And swap with the current index

        leftChildIndex = self.getLeftChildIndex(index)
        rightChildIndex = self.getRightChildIndex(index) 

        smallestValIndex = index 
        if (leftChildIndex < len(self.data) ) and (self.data[leftChildIndex] < self.data[smallestValIndex] ):
            smallestValIndex = leftChildIndex
        if (rightChildIndex < len(self.data) ) and (self.data[rightChildIndex] < self.data[smallestValIndex] ):
            smallestValIndex = rightChildIndex
        
        if smallestValIndex != index:
            self.swapTwoIndexValues( smallestValIndex, index )
            self.heapify( smallestValIndex )

    def getMin(self):
        return self.data[ 0 ]
    
    def extractMin(self):
        minValueToReturn = self.data[0]

        #get the last value in the heap and place in the first index. And then remove the last element
        self.data[ 0 ] = self.data[ len(self.data) - 1 ]
        self.data.pop()

        # Call the heapify function at the first index
        self.heapify( 0 )

        return minValueToReturn

    def delete(self, index):
        # Here I am not doing the same as mentioned in the blog.
        # What i am thinking to do is the same logic which is used in extractMin function. And I believe this would be also be giving correct result in all scenario

        self.data[index] = self.data[ len(self.data) - 1 ]
        self.data.pop()

        self.heapify( index )
