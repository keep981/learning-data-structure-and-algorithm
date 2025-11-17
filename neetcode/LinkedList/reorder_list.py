from .myLinkedListHelper import printTheLinkedList
import time

# Leetcode-143

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        return self.reorderListMyApproach_1(head)
    
    def reorderListMyApproach_1(self, head):
        if head is None:
            return None

        newListHead = head
        newListTail = head
        oldListHead = head.next

        while oldListHead is not None:
            #Phase1 - will iterate from the oldListHead till the last node and add that to newListTail
            backwardPointer = oldListHead
            forwardPointer = oldListHead.next #this is actually the ahead pointer in the two pointer approach. ultimateLastNodeOfOldList
            if forwardPointer is not None: #If it will be None means in the current iteration of oldList there is only one node left, we will add that node in next phase. If it will be not None means more than or equal to two elements will be there in the current iteration oldList
                while forwardPointer.next is not None:
                    backwardPointer = forwardPointer
                    forwardPointer = forwardPointer.next

                
                newListTail.next = forwardPointer
                newListTail = forwardPointer
                backwardPointer.next = None   # This assignement is needed to identify this node to be the last node int he next iteration

            #Phase2 - will just add the add the the oldListhead to the end of newListTail 
            newListTail.next = oldListHead
            newListTail = oldListHead
            oldListHead = oldListHead.next

        
        #At first it will look like in the end we have to do the newListTail.next = None, But actually it will be taken care in the first phase asignment of backWardPointer.next to None.If you will do dry run with of 1 + (1/2/3/4) nodes you will see that , here the first 1 means that one we set before the first while loop. In other words every last pointer will be get the chance of becoming secondLast pointer. For 1 + 1 node, the second element will already have its next as None.

        return newListHead


if __name__ == "__main__":
    print("running abcd.py as module")
    noOfElem = int(input())
    print(f"noOfElem = {noOfElem}")
    inputLinkedListHead = ListNode(val = -999999)  #Dummy List initializing
    listTail = inputLinkedListHead
    while noOfElem > 0:
        num = int(input())
        newNode = ListNode(val = num)
        listTail.next = newNode
        listTail = newNode

        noOfElem-=1
    inputLinkedListHead = inputLinkedListHead.next

    # printTheLinkedList( inputLinkedListHead )
    start = time.time()
    ansHead = Solution().reorderList( inputLinkedListHead )
    end = time.time()

    print( end - start )

