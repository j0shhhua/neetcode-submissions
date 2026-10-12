class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        cursum = 0
        for r in range(len(arr)):
            cursum += arr[r]
            while (r - l + 1) > k:   # shrink if window exceeds k
                cursum -= arr[l]
                l += 1
            if (r - l + 1) == k:     # exactly k elements
                if (cursum / k) >= threshold:
                    res += 1
        return res