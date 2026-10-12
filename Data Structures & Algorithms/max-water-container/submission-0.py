class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) == 1:
            return None
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            dist = r - l
            multiply = min(heights[l], heights[r])
            ans = multiply * dist
            res = max(res, ans)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res