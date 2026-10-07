class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        # dummy nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node: Optional[Node]) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev      
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # remove at specific node
        node = self.cache[key]
        self.remove_node(node)

        # insert in tail
        node = self.insert_at_end(key, node.val)
        self.cache[key] = node

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove at specific node
            node = self.cache[key]
            self.remove_node(node)
            self.size -= 1

        elif self.size == self.capacity:
                # remove at head
                lru_node = self.head.next
                self.cache.pop(lru_node.key)
                self.remove_node(lru_node)
                self.size -= 1

        # insert in tail
        node = self.insert_at_end(key, value)
        self.cache[key] = node
        self.size += 1

    ####

    # return head
    def insert_at_front(self, head: Optional[Node], key, val) -> Optional[Node]:
        node = Node(key, val, head, None)
        if head:
            head.prev = node
        else:
            self.tail = node 
        return node
    
    def insert_at_end(self, key, val) -> Node:
        node = Node(key, val)

        real_tail = self.tail.prev

        # insert node between real_tail and tail
        real_tail.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = real_tail

        return node

    # return head
    def remove_at_front(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        if head.next: 
            head.next.prev = None
        else:
            self.tail = None 
        head = head.next
        return head
    

  



