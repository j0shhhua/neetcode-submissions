class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bruteforce(row, col, m, n):
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1

            return bruteforce(row + 1, col, m, n) + bruteforce(row, col + 1, m, n)

        return bruteforce(0, 0, m, n)
        