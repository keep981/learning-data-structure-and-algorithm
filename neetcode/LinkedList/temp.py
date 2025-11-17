class LRUCache(object):
    class ListNode(object):
        def __init__(self, key, prev=None, next=None):
            self.key:int = key
            self.prev = prev
            self.next = next

    class KeyInfo(object):
        def __init__(self, value, listNodeObj):
            self.value:int = value
            self.listNodeObj = listNodeObj


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashTab = dict()

        
        self.head = self.ListNode(-1)
        self.tail = self.head #This i missed in first go, in case of single capacity tail will be the head 
        self.hashTab[-1] = self.KeyInfo( -1, self.head )  #Intializing with same value as key
        prevNodeItr = self.head
        for itr in range(2, capacity + 1, 1):
            tempNode = self.ListNode(-itr)
            prevNodeItr.next = tempNode
            tempNode.prev = prevNodeItr
            self.hashTab[-itr] = self.KeyInfo( -itr, tempNode )       

            prevNodeItr = tempNode
            self.tail = tempNode #This i missed
            
    def helperMovingGivenNodeToEndInDoublyLinkedList(self, nodeToMove):
        # This does not check if the nodeToMove exist in linkedlist it self or not. it expects the nodeToMove should be there
        if nodeToMove is self.tail:
            # nodeToMove is already at tail position, so nothing to do
            # If you observe size One Doubly linked list is also handled here, because there the head and tail will be the nodeToMove itself
            return 

        elif nodeToMove is self.head:
            #No need to worry about where head is same as tail, it is handled above
            self.head = self.head.next
            self.head.prev = None
            nodeToMove.next = None
            nodeToMove.prev = self.tail
            self.tail.next = nodeToMove
            self.tail = nodeToMove
            return
        else:
            #nodeToMove is somewhere in the middle
            nodeToMove.prev.next = nodeToMove.next
            nodeToMove.next.prev = nodeToMove.prev

            nodeToMove.next = None
            nodeToMove.prev = self.tail
            self.tail.next = nodeToMove
            self.tail = nodeToMove



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.hasTab:
            return -1
        
        #Key is present
        #Send the listNodeObj to the to the tail of the doubly linked list

    
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)        

def printTheDoublyLinkedList(head):
    while head:
        strForCurNode = ""
        if not head.prev:
            strForCurNode += "None<-->"
        else:
            strForCurNode += f"{head.prev.key}<-->"

        strForCurNode += f"{head.key}<-->"

        if not head.next:
            strForCurNode += "None"
        else:
            strForCurNode += f"{head.next.key}"

        print(strForCurNode)
        head = head.next



if __name__ == "__main__":
    print("Hi")

    obj = LRUCache(8)

    printTheDoublyLinkedList(obj.head)
    print( f"🤩{obj.head.key} {obj.tail.key}"  )
    print("😎😎😎😎")

    obj.helperMovingGivenNodeToEndInDoublyLinkedList( obj.hashTab[-1].listNodeObj )
    printTheDoublyLinkedList(obj.head)

    print( f"🤩{obj.head.key} {obj.tail.key}"  )




    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)