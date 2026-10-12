class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stuff = [-s for s in nums]
        heapq.heapify(stuff)
        while k > 0:
            res = heapq.heappop(stuff)
            k -= 1
        return -(res)