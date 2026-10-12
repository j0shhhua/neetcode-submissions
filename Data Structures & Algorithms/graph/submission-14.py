from collections import deque
class Graph:
    
    def __init__(self):
        self.arr = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.arr:
            self.arr[src] = set()
        if dst not in self.arr:
            self.arr[dst] = set()
        self.arr[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.arr or dst not in self.arr[src]:
            return False
        self.arr[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._bfs(src, dst, visited)
    
    def _bfs(self, curr, dst, visited):
        q = deque()
        q.append(curr)
        visited.add(curr)
        while q:
            node = q.popleft()
            if node == dst:
                return True
            else:
                for i in self.arr.get(node, None):
                    if not i:
                        continue
                    q.append(i)
        return False
            
                
