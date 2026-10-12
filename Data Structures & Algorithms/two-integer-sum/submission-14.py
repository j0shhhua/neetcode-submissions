class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        i = 0
        for num in nums:
            mapping[num] = i
            i += 1
        
        for j in range(len(nums)):
            res = target - nums[j]
            if res in mapping and j != mapping[res]:
                return [j, mapping[res]]
        
            