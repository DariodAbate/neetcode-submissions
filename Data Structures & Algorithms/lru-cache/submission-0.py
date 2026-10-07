class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # remove at specific node
        node = self.cache[key]
        self.remove_node(node)

        # insert in tail
        self.tail = self.insert_at_end(self.tail, key, node.val)
        self.cache[key] = self.tail

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove at specific node
            node = self.cache[key]
            self.remove_node(node)
            self.size -= 1

        elif self.size == self.capacity:
                # remove at head
                self.cache.pop(self.head.key)
                self.head = self.remove_at_front(self.head)
                self.size -= 1

        # insert in tail
        self.tail = self.insert_at_end(self.tail, key, value)
        self.cache[key] = self.tail
        self.size += 1

    ####

    # return head
    def insert_at_front(self, head: 'Optional[Node]', key, val) -> 'Optional[Node]':
        node = Node(key, val, head, None)
        if head:
            head.prev = node
        else:
            self.tail = node 
        return node
    
    # return tail
    def insert_at_end(self, tail: 'Optional[Node]', key, val) -> 'Optional[Node]':
        node = Node(key, val, None, tail)
        if tail:
            tail.next = node
        else:
            self.head = node 
        return node

    # return head
    def remove_at_front(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if head.next: 
            head.next.prev = None
        else:
            self.tail = None 
        head = head.next
        return head
    
    # return tail
    def remove_at_tail(self, tail: 'Optional[Node]') -> 'Optional[Node]':
        if not tail:
            return None
        if tail.prev: 
            tail.prev.next = None
        else:
            self.head = None         
        tail = tail.prev
        return tail

    def remove_node(self, node: 'Optional[Node]') -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None            



class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev