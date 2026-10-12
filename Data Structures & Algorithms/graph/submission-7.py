class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for i in self.adj_list.get(src,[]):
            if self._dfs(i, dst, visited):
                return True
        return False

