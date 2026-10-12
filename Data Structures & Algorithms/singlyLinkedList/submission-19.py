class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next 
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        new = Node(val)
        self.tail.next = new
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
