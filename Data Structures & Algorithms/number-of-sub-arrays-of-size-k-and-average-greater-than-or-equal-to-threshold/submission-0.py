class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        cur = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            cur += arr[L+k-1]
            if (cur/k) >= threshold:
                res += 1
            cur -= arr[L]
        return res
            