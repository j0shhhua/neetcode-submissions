class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        q = deque()
        visit = set((0, 0))
        q.append((0, 0, 1))
        
        while q:
            r, c, length = q.popleft()
            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit and grid[nr][nc] == 0):
                    q.append((nr, nc, length + 1))
                    visit.add((nr, nc))
        return -1