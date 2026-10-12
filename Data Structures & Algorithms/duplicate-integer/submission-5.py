class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = []
        for num in nums:
            if num in checker:
                return True
            checker.append(num)
        return False