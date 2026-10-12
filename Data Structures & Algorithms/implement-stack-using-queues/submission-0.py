class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = Node(-1)

    def push(self, x: int) -> None:
        nxt, prv = self.head.next, self.head
        new_node = Node(x)
        new_node.next, prv.next = nxt, new_node

    def pop(self) -> int:
        res = self.head.next
        nxt, prv = self.head.next.next, self.head
        prv.next = nxt
        return res.val

    def top(self) -> int:
        return self.head.next.val

    def empty(self) -> bool:
        if self.head.next == None:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()