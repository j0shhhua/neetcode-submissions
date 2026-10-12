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
        if not self.arr[pos]:
            self.arr[pos] = Node(key, value)
            self.size += 1
        else:
            prv = None
            curr = self.arr[pos]
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prv, curr = curr, curr.next
            prv.next = Node(key,value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.arr[index]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        curr = self.arr[index]
        prv = None

        while curr:
            if curr.key == key:
                if prv:
                    prv.next = curr.next
                else:
                    self.arr[index] = curr.next
                self.size -= 1
                return True
            prv, curr = curr, curr.next
        return False    

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

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

