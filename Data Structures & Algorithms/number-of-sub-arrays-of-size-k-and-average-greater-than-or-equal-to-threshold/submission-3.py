class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        cursum = 0
        res = 0

        for R in range(len(arr)):
            cursum += arr[R]
            if R - L + 1 < k:
                continue
            else:
                if (cursum / k) >= threshold:
                    res += 1
                cursum -= arr[L]
                L += 1
                
        return res
                