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

    def hashing(self, key):
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        idx = self.hashing(key)
        new = Node(key, value)

        if not self.cache[idx]:
            self.cache[idx] = new
            self.size += 1
        else:
            prev = None
            curr = self.cache[idx]
            while curr:
                if curr.key == key:
                    curr.val = value
                    return
                prev, curr = curr, curr.next
            prev.next = new
            self.size += 1
         
        if (self.size / self.capacity) >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        idx = self.hashing(key)
        curr = self.cache[idx]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        idx = self.hashing(key)
        curr = self.cache[idx]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.cache[idx] = curr.next
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_map = [None] * self.capacity

        for i in self.cache:
            if i:
                idx = self.hashing(i.key)
                if not new_map[idx]:
                    new_map[idx] = i
                else:
                    new_map[idx] = curr
                    while curr and curr.next:
                        curr = curr.next
                    curr.next = i

        self.cache = new_map 
