# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # case where need to remove the first element
        dummy = ListNode(0, head) 
        
        l = dummy
        r = head

        # r is n positions ahead l  
        for i in range(0, n):
            r = r.next

        # when r points to the last element
        # l points to the prev of the element
        # to remove
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next

        return dummy.next
        

        