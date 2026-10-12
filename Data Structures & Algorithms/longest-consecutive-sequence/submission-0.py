class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = 0
        for num in nums:
            beta = 0
            i = num
            while i in nums:
                i += 1
                beta += 1
            size = max(size, beta)
        return size
        