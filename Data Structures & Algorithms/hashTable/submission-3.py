class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = [None] * self.capacity

    def hash_value(self, key):
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        index = self.hash_value(key)
        node = self.cache[index]
        prev = None

        if node:
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        else:
            self.cache[index] = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_value(key)
        node = self.cache[index]

        if node:
            while node:
                if node.key == key:
                    return node.value
                node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_value(key)
        node = self.cache[index]
        prev = None

        if node:
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next
                        self.size -= 1
                    else:
                        self.cache[index] = node.next
                    self.size -= 1
                    return True
                prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_cache = [None] * new_capacity

        for node in self.cache:
            while node:
                index = self.hash_value(node.key)
                if new_cache[index] is None:
                    new_cache[index] = Node(node.key, node.value)
                else:
                    new = new_cache[index]
                    while new_node.next:
                        new = new.next
                    new.next = Node(node.key, node.value)
                node = node.next
        self.capacity = new_capacity
        self.cache = new_cache

