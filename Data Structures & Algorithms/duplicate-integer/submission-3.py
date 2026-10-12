class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         if len(nums) == 0:
            return False
         
         control = nums[0]
         sorted_nums = sorted(nums)
         for num in range(1, len(sorted_nums)):
            if control == sorted_nums[num]:
                return True
            control = sorted_nums[num]
         return False
        
        

        
            