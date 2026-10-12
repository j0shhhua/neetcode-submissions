class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, j in enumerate(nums):
            indices[j] = i

        for i, j in enumerate(nums):
            diff = target - j
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
            
            
            
           
        
            
