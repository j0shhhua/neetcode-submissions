class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i, j in enumerate(nums):
            res = target - j
            if res in count:
                return [count[res], i]
            else:
                count[j] = i