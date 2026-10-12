class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i  = 0
        while curr:
            if i == index:
                return curr.data
            i += 1
            curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next
        while curr:
            ans.append(curr.data)
            curr = curr.next
        return ans
        
