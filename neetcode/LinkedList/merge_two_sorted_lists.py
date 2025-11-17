# Question - Leetcode 21- https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # return self.mergeTwoListsIterative(list1, list2)
        return self.mergeTwoListsRecursive_Approach1(list1, list2)


    def mergeTwoListsRecursive_Approach1(self, list1, list2):
        # Base Case
        if (list1 is None):
            return list2
        elif (list2 is None):
            return list1

        #Will find solution for current call
        ##We are at this line of the current function call means both of the list will have atleast one element
        headAtThisCallStack = None
        if list1.val < list2.val:
            headAtThisCallStack = list1
            list1 = list1.next
        else:
            headAtThisCallStack = list2
            list2 = list2.next
    
       
        # Will give subproblem to solve it self 
        subProblemHeadAtThisCallStack = self.mergeTwoListsRecursive_Approach1(list1, list2)

        #Current callStackHead will point to head of subProblemCallStack head
        headAtThisCallStack.next = subProblemHeadAtThisCallStack

        return headAtThisCallStack

    def mergeTwoListsIterative(self, list1, list2):
        #if either of the list is empty i.e is None, the other list will be as it is the answer
        if (list1 is None):
            return list2
        elif (list2 is None):
            return list1

        head = None
        curTailPtr = None
        #We have reached here means both of the list will have atleast one element. Will determine the new head here and also initialize the curTailPtr.
        if list1.val < list2.val:
            head = list1
            curTailPtr = list1
            list1 = list1.next
        else:
            head = list2
            curTailPtr = list2
            list2 = list2.next
        
        #will keep on adding the rest elements to the tail ptr.
        while True:
            if list1 is None:
                curTailPtr.next = list2
                break
            elif list2 is None:
                curTailPtr.next = list1
                break
            
            if list1.val < list2.val:
                curTailPtr.next = list1
                curTailPtr = list1
                list1 = list1.next
            else:
                curTailPtr.next = list2
                curTailPtr = list2
                list2 = list2.next

        
        return head