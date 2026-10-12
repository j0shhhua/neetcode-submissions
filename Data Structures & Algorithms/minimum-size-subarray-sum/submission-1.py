class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsub = float("inf")
        cur, L = 0,0

        for R in range(len(nums)):
            cur += nums[R]
            while cur >= target:
                minsub = min(minsub, R - L + 1)
                cur -= nums[L]
                L += 1
        return 0 if minsub == float("inf") else minsub