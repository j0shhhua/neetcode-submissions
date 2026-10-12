class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.size = 0

    def hash(self, key):
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        pos = self.hash(key)
        node = self.arr[pos]
        if not node:
            self.arr[pos] = Node(key, value)
            self.size += 1
        else:
            prv = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                prv = node
                node = node.next
            prv.next = Node(key, value)
            self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        pos = self.hash(key)
        curr = self.arr[pos]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        pos = self.hash(key)
        curr = self.arr[pos]
        prv = None
        if not curr:
            return False
        while curr:
            if curr.key == key:
                if not prv:
                    self.arr[pos] = self.arr[pos].next
                    self.size -= 1
                    return True
                if not curr.next:
                    prv.next = None
                    self.size -= 1
                    return True
                prv.next = curr.next
            prv = curr
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    # Might need to revisit
    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for node in self.arr:
            while node:
                index = node.key % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.val)
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.val)
                node = node.next

        self.capacity = new_capacity
        self.arr = new_table
