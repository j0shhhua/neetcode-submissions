class Deque:
    
    def __init__(self):
        self.q = []

    def isEmpty(self) -> bool:
        if len(self.q) <= 0:
            return True
        return False

    def append(self, value: int) -> None:
        self.q.append(value)

    def appendleft(self, value: int) -> None:
        self.q.insert(0, value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.q.pop()
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.q.pop(0)
        return val
