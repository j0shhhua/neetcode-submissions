class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = []
        for i in nums:
            if i in count:
                return True
            else:
                count.append(i)
        return False