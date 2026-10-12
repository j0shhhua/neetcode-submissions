class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visit = {}
        l, res = 0, 0
        maxf = 0
        for r in range(len(s)):
            visit[s[r]] = 1 + visit.get(s[r], 0)
            maxf = max(maxf, visit[s[r]])
            while (r-l+1) - maxf > k:
                visit[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res