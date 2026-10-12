class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = {}
        for num in nums:
            if num not in checker:
                checker[num] = 1
            else:
                return True
        return False