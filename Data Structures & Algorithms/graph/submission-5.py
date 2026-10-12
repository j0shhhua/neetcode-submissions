class Graph:
    
    def __init__(self):
        self.adj_list = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True


    def _dfs(self, src: int, dst: int, visit) -> bool:
        if src == dst:
            return True
        visit.add(src)
        for neighbour in self.adj_list.get(src, []):
            if neighbour not in visit:
                if self._dfs(neighbour, dst, visit):
                    return True
        return False

    def hasPath(self, src, dst):
        visit = set()
        return self._dfs(src, dst, visit)

