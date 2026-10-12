class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        length = 0

        queue.append((0, 0))
        visit.add((0, 0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length

            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

            for dr, dc in directions:
                if ((min((dr + r, dc + c)) < 0) or (dr + r) == ROW or (dc + c) == COL or (dr + r, dc + c) in visit or grid[dr + r][dc + c] == 1):
                    continue
                visit.add((dr + r, dc + c))
                queue.append((dr + r, dc + c))
            length += 1
        return -1