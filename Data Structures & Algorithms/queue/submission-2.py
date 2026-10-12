class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        nxt, prv = self.tail, self.tail.prev
        new_node.next, new_node.prev = nxt, prv
        nxt.prev, prv.next = new_node, new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        nxt, prv = self.head.next, self.head
        new_node.next, new_node.prev = nxt, prv
        nxt.prev, prv.next = new_node, new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        res = self.tail.prev
        nxt, prv = self.tail, self.tail.prev.prev
        prv.next, nxt.prev = nxt, prv
        return res.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        res = self.head.next
        nxt, prv = self.head.next.next, self.head
        nxt.prev, prv.next = prv, nxt
        return res.val
        
