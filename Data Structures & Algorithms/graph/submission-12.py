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
        return self._dfs(src, dst, visited)
    
    def _dfs(self, curr, dst, visited):
        if curr == dst:
            return True
        visited.add(curr)
        for i in self.arr.get(curr, []):
            if i not in visited:
                if self._dfs(i, dst, visited):
                    return True
        return False
                
