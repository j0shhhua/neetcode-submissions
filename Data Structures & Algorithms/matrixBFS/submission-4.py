class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        q.append((0, 0))
        length = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if(r == ROWS - 1 and c == COLS - 1):
                    return length

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visit):
                        continue
                    q.append((nr, nc))
                    visit.add((nr, nc))
            length += 1

        return -1