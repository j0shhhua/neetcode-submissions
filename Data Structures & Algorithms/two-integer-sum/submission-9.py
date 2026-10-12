class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_list = {}
       for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_list:
                return [num_list[diff], i]
            num_list[nums[i]] = i
        

       
            
            
            
           
        
            
