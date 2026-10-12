class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count or not self.head.next:
            return -1
        curr = self.head.next
        count = 0
        while curr.next and count != index:
            curr = curr.next
            count += 1
        return curr.val

    def insertHead(self, val: int) -> None:
        if not self.head.next:
            self.head.next = Node(val)
            self.count += 1
            return
        new = Node(val)
        prev, next = self.head, self.head.next
        prev.next, new.next = new, next
        self.count += 1
        return

    def insertTail(self, val: int) -> None:
        if not self.head.next:
            self.head.next = Node(val)
            self.count += 1
            return
        curr = self.head.next
        new = Node(val)
        while curr.next is not None:
            curr = curr.next
        curr.next = new
        self.count += 1
        return

    def remove(self, index: int) -> bool:
        if not self.head.next or index >= self.count:
            return False
        count = 0
        nxt = self.head.next
        prv = self.head
        while nxt.next is not None and count != index:
            nxt = nxt.next
            prv = prv.next
            count += 1 
        if not nxt.next:
            prv.next = prv.next.next
        else:
            prv.next = nxt.next
        self.count -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return res
