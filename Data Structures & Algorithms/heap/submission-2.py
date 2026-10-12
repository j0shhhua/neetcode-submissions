class MinHeap:
    
    def __init__(self):
        self.nums = []

    def push(self, val: int) -> None:
        heapq.heappush(self.nums, val)

    def pop(self) -> int:
        if not self.nums:
            return -1
        return heapq.heappop(self.nums)

    def top(self) -> int:
        if not self.nums:
            return -1
        return self.nums[0]

    def heapify(self, nums: List[int]) -> None:
        heapq.heapify(nums)
        self.nums = nums
        