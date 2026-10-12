class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-i for i in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            if second > first:
                heapq.heappush(nums, first - second)
        
        if not nums:
            return 0
        else:
            return abs(nums[0])
