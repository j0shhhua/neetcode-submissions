class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

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
        if self.isEmpty():
            self.head.next = Node(value)
            self.head.next.prev = self.head
            self.tail.prev = self.head.next
            self.head.next.next = self.tail
        else:
            new_node = Node(value)
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            new_node.prev.next = new_node
            self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.head.next = Node(value)
            self.head.next.prev = self.head
            self.tail.prev = self.head.next
            self.head.next.next = self.tail
        else:
            new_node = Node(value)
            new_node.prev, new_node.next = self.head, self.head.next
            self.head.next.prev, self.head.next = new_node, new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            val = self.tail.prev.val
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            val = self.head.next.val
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            return val

        
