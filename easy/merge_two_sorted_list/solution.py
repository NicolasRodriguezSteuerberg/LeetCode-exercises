from typing import List, Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    '''Manera bruta total
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headList: Optional[ListNode] = None

        # if one of the two list are none return the other
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val > list2.val:
            headList = list2
            list2 = list2.next
        else:
            headList = list1
            list1 = list1.next
        mergedList = headList
        while list1 is not None or list2 is not None:
            if list1.val < list2.val:
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            mergedList = mergedList.next
        while(list1 is not None):
            mergedList.next = list1
            list1 = list1.next
            mergedList = mergedList.next
        while(list2 is not None):
            mergedList.next = list2
            list2 = list2.next
            mergedList = mergedList.next
        return headList
    '''


    '''Mejor manera'''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = nodeList = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                nodeList.next = list1
                list1 = list1.next
                # list1, nodeList = list1.next, nodeList.next
            else:
                nodeList.next = list2
                list2 = list2.next
            nodeList = nodeList.next
        if list1 or list2:
            nodeList.next = list1 if list1 else list2 # si hay list1 añadimos list1 si no list2
        # we only need an if statement because, for insance,
        # if list1 has 2 values remaining the nodeList.next pointer will take the first remaining value from list1.
        # Since this pointer already points to the next node, there is no need to execute the "if" block again or change it to a while
        return dummy.next # por que el primero está vacio