def printTheLinkedList(head):
    while head:
        print(head.val, "->", end="")
        head = head.next
    
    print()


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


