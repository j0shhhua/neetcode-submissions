class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = len(numbers) - 1
        while True:
            stuff = target - numbers[track]
            if stuff in numbers:
                return [numbers.index(stuff) + 1 ,track + 1]
            track -= 1
            