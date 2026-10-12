class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return self.binary_search(matrix[i], target)
            continue
        return False
    
    def binary_search(self, lis, targ):
        L = 0
        R = len(lis) - 1

        while L <= R:
            mid = (L + R) // 2

            if lis[mid] < targ:
                L = mid + 1
            elif lis[mid] > targ:
                R = mid - 1
            else:
                return True
        return False