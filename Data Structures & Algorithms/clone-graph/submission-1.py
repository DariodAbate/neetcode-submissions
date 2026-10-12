"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        root = node
        
        # create the new nodes
        addresses = {}
        q = deque([node])
        addresses[node] = Node(node.val)
        while q:
            node = q.popleft()
            
            for n in node.neighbors:
                if n not in addresses:
                    q.append(n)
                    # register here, so  i do not enqueue the same node multuple times
                    addresses[n] = Node(n.val) 
                addresses[node].neighbors.append(addresses[n])
                
        return addresses[root]
        