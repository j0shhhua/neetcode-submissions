class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, grid, visit):
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r, c) in visit):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))

            count = 0
            count += dfs(r + 1, c, grid, visit)
            count += dfs(r - 1, c, grid, visit)
            count += dfs(r, c + 1, grid, visit)
            count += dfs(r, c - 1, grid, visit)

            visit.remove((r, c))
            return count
        return dfs(0, 0, grid, set())