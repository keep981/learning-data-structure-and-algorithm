# Leetcode-19
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #First approach, brute force solution will be first iterate the linked list completely and get the count. Then in the second pass we will iterate (count-n) nodes from the beginning and from that node we will remove the desired node. I can do this, so not doing 

        #Second approach, we will be using the two pointers concept, so that we will be able to do in one pass
        skipCount = n
        forwardPointer = head
        #Will skip n -1 nodes after head, because we will start from head 
        while skipCount > 0:
            forwardPointer = forwardPointer.next
            skipCount-= 1

        if forwardPointer is None:
            #Means, n is the length of the linkedlist, i.e to remove the first element i.e. from the starting of the linked list
            head = head.next
            return head
        else:
            backwardPointer = head
            while forwardPointer.next is not None:
                backwardPointer = backwardPointer.next
                forwardPointer = forwardPointer.next

            backwardPointer.next = backwardPointer.next.next

            return head
            