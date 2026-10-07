# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        l = head
        while l:
            size += 1
            l = l.next

        if size == n:
            return head.next

        l = head
        prev = None
        for i in range(0, size - n):
            prev = l
            l = l.next
     
        prev.next = l.next

        return head

        

        