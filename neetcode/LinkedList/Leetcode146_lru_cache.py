
#******************************* My Approach 1, using array to perform the operation**********************#
# both put and get operation are of BigO( n ) time complexity. This is producing correct result but O(1) complexity is needed"

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        class Info:
            def __init__(self, key, value, ageBit):
                self.key = key
                self.value = value
                self.ageBit = ageBit

        self.capacity = capacity
        self.Info = Info
        self.listCache = []    
        for i in range(0, capacity):  #doing this to not check the capacity each operation, initializing with dummy data
            self.listCache.append( Info(-1, -1, -1) )

        self.operationCount = 0 #At most 2  10^5 calls would be made, so it will come within integer range, if there was no such constraint then what we could have done is once operation count reaches the integer max, then we would have sorted the listCache elements in the increasing order of age bit. As this sorting won't be taking much time as our capacity won't be huge. And then we will iterate the items and update their age bit by +1 of their previous item and then set operationCount to capacity. Actuallu datetime i was thiking to use for the ageBit but after reading the wikipedia link given in the question description using the integer value. 



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        #if the key is present, Two things to do i) return the value ii) also update the age bit 
        for i in range(0, self.capacity):
            if self.listCache[i].key == key:
                self.listCache[i].ageBit =  self.operationCount
                self.operationCount += 1
                return self.listCache[i].value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # as the approach i have used is to initialize with the capacity with dummy nodes, even if the listCache is not filled with real records, i.e ther is still  dummy nodes exist at that time also we will perform the eviction
        oldestElemIndex = 0
        currentKeyIndexIfExist = -1
        for i in range(0, self.capacity):
            if self.listCache[i].key == key:
                currentKeyIndexIfExist = i
            
            if self.listCache[i].ageBit < self.listCache[oldestElemIndex].ageBit:
                oldestElemIndex = i

        if currentKeyIndexIfExist != -1:
            #Key already there so we will update it's value and ageBit
            self.listCache[currentKeyIndexIfExist].value = value
            self.listCache[currentKeyIndexIfExist].ageBit = self.operationCount
        else:
            #We will perform the evict operation
            self.listCache[oldestElemIndex] =  self.Info(key, value, self.operationCount  )

        self.operationCount += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#******************************* My Approach 1 Ends ****************************#
