class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax=globmin=nums[0]
        curmax=curmin=total=0

        for i in nums:
            curmax=max(curmax+i,i)
            globmax=max(globmax,curmax)
            curmin=min(curmin+i,i)
            globmin=min(globmin,curmin)
            total+=i
        return max(globmax,total-globmin) if globmax>0 else globmax