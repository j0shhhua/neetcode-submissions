class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cursum = 0
        res = 1000
        for r in range(len(nums)):
            cursum += nums[r]
            if cursum >= target:
                while cursum >= target:
                    res = min(res,(r-l+1))
                    cursum -= nums[l]
                    l+=1
        return 0 if res == 1000 else res