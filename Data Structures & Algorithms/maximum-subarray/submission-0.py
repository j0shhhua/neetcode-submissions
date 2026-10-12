class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxcurr = nums[0]
        for i in nums:
            curr = max(curr, 0)
            curr += i
            maxcurr = max(maxcurr, curr)
        return maxcurr