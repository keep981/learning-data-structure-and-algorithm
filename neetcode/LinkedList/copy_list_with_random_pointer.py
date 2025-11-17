# Question - Leetcode 138- https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self.copyRandomList_MyApproach1(head)
    
    def copyRandomList_MyApproach1(self, head):
        #brute force approach
        #First we will just clone the linked list without setting the values of random value
        #In the second pass we will start from the head and iterate the nodes one by one. At that time from the old list, we will get the position of the random pointer node from the end ,suppose called x. So for setting the value of random pointer in the new linked list, we will get the node with xth position from the end in the new linked list. And set the value of random pointer.
        #This will be of time complexity n^2. i.e outer loop n and then within loop n + n. so n^2 it will be.
        # -----------------------------------------------
        if head is None:
            return None

        #cloning without setting value for random
        newHead = Node(head.val)  
        prevNewNode =  newHead
        nodeItrOld = head.next
        while nodeItrOld:
            tempNode = Node(nodeItrOld.val)           
            prevNewNode.next = tempNode 
            prevNewNode = tempNode
            nodeItrOld = nodeItrOld.next

        # setting the random memeber variable value
        nodeItrNewLinkedList = newHead
        nodeItrOldLinedList = head
        while nodeItrNewLinkedList:
            if nodeItrOldLinedList.random is None:
                nodeItrNewLinkedList.random = None
            else:
                positionFromEndOfRandomPointerOfOldList = self.helper_getPositionFromEnd(nodeItrOldLinedList.random)
                nodeItrNewLinkedList.random = self.helper_getXthPositionNodeEnd(newHead, positionFromEndOfRandomPointerOfOldList)

            nodeItrOldLinedList = nodeItrOldLinedList.next
            nodeItrNewLinkedList = nodeItrNewLinkedList.next

        return newHead
        
    def helper_getPositionFromEnd(self, node):
        position = 0
        while node:
            position += 1
            node = node.next
        
        return position

    def helper_getXthPositionNodeEnd(self, head, position):
        #This function does not handle the cases if position sent is greater than the actual length of the linked list. Or None value in head

        #We will be using the two pointers approach
        nodeItr = head
        while position > 0:
            nodeItr = nodeItr.next
            position-=1
        
        ansNode = head
        while nodeItr:
            ansNode = ansNode.next
            nodeItr = nodeItr.next

        return ansNode



