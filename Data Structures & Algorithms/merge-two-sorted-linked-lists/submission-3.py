# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        newList = None
        if list1.val <= list2.val:
            newList = list1
            currl1 = list1.next
            currl2 = list2
        else:
            newList = list2
            currl1 = list1
            currl2 = list2.next

        curr = newList
        while currl1 or currl2:
            if not currl2 or (currl1 and currl1.val <= currl2.val):
                self.addNode(curr, currl1.val)
                currl1 = currl1.next
            else:
                self.addNode(curr, currl2.val)
                currl2 = currl2.next
            curr = curr.next


        return newList
    
    def addNode(self, curr: Optional[ListNode], val):
        n = ListNode(val)
        curr.next = n


        