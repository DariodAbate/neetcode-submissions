# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newList = None
        currl1 = list1
        currl2 = list2

        while currl1 or currl2:
            if not currl2 or (currl1 and currl1.val <= currl2.val):
                newList = self.addNode(newList, currl1.val)
                currl1 = currl1.next
            else:
                newList = self.addNode(newList, currl2.val)
                currl2 = currl2.next


        return newList
    
    def addNode(self, l: Optional[ListNode], val) -> Optional[ListNode]:
        n = ListNode(val)
        if l is None:
            return n
        
        curr = l
        while curr.next:
            curr = curr.next
        curr.next = n

        return l
        