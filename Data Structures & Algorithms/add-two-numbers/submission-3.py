# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        rem = 0

        dummy = ListNode(0, None)
        ret = dummy
        while curr1 or curr2 or rem > 0:
            a = curr1.val if curr1 else 0
            b = curr2.val if curr2 else 0

            sum = a + b + rem
            rem = sum // 10
            dummy.next = ListNode(sum % 10)

            dummy = dummy.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None


        return ret.next
            
        