from collections import deque
class Deque:
    
    def __init__(self):
        self.arr = deque()

    def isEmpty(self) -> bool:
        if not self.arr:
            return True
        return False

    def append(self, value: int) -> None:
        self.arr.append(value)

    def appendleft(self, value: int) -> None:
        self.arr.appendleft(value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr.pop()

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr.popleft()
