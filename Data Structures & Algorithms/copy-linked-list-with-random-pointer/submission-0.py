"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dumb = Node(0, None, None)
        ret = dumb

        # copy the list and initialize correct next pointers
        # store the positions in a set: associate node with its position
        l = head
        pos = 0
        addToPos = {}
        posToNewAdd = {}
        while l:
            addToPos[l] = pos

            dumb.next = Node(l.val, None, None)
            l = l.next
            dumb = dumb.next
            posToNewAdd[pos] = dumb

            pos += 1

        
        # initialize the random pointers
        # by using the maps 
        dumb = ret
        l = head
        dumb = dumb.next # discard first element
        pos = 0
        while dumb:
            if l.random:
                dumb.random = posToNewAdd[addToPos[l.random]]
            else:
                dumb.random = None

            dumb = dumb.next
            l = l.next
        return ret.next




        