import heapq
class MinHeap:
    
    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        if not self.arr:
            self.arr.append(val)
            heapq.heapify(self.arr)
        else:
            heapq.heappush(self.arr, val)

    def pop(self) -> int:
        if not self.arr:
            return -1
        return heapq.heappop(self.arr)

    def top(self) -> int:
        if not self.arr:
            return -1
        return self.arr[0]

    def heapify(self, nums: List[int]) -> None:
        heapq.heapify(nums)
        self.arr = nums