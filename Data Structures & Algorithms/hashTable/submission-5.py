class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.cache = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def hash_value(self, key):
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        index = self.hash_value(key)

        if not self.cache[index]:
            self.cache[index] = Node(key, value)
            self.size += 1
        else:
            curr = self.cache[index]
            prev = None
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev, curr = curr, curr.next
            prev.next = Node(key, value)
            self.size += 1
        
        if (self.size / self.capacity) >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_value(key)
        curr = self.cache[index]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_value(key)
        curr = self.cache[index]
        prev = None

        while curr:
            if curr.key == key:
                if not prev:
                    self.cache[index] = curr.next
                    self.size -= 1
                    return True
                else:
                    prev.next = curr.next
                    self.size -= 1    
                    return True
            prev, curr = curr, curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_cache = [None] * self.capacity

        for node in self.cache:
            while node:
                new_index = self.hash_value(node.key)
                if not new_cache[new_index]:
                    new_cache[new_index] = Node(node.key, node.val)
                else:
                    prev = None
                    curr = new_cache[new_index]
                    while curr:
                        prev, curr = curr, curr.next
                    prev.next = Node(node.key, node.val)
                node = node.next
        
        self.cache = new_cache
