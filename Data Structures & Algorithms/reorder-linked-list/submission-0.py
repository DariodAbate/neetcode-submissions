# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return

        slow = head
        fast = head

        # find half of the list
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None # cut the original list

        l = head
        r = slow

        # reverse the last half
        r = self.reverseList(r)

        # merge the two lists in alternating order
        dummy = ListNode()
        curr = dummy

        while r and l:
            curr.next = l
            l = l.next
            curr = curr.next

            curr.next = r
            r = r.next
            curr = curr.next
        curr.next = r or l

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next
        
        return prev

         
        
        
        