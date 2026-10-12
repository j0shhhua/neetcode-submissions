class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        l, r = 0, len(nums)
        k = len(nums)
        while l < r:
            if nums[l] in seen:
                nums.pop(l)
                r = len(nums)
                k -= 1
                continue
            seen.add(nums[l])
            l+=1
        print(nums)
        return k
