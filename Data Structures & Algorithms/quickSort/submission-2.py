# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs


    def quickSortHelper(self, array, s, e):
        if e - s + 1 <= 1:
            return

        pivot = array[e]
        left = s

        for i in range(s, e):
            if array[i].key < pivot.key:
                tmp = array[left]
                array[left] = array[i]
                array[i] = tmp
                left += 1
        
        array[e] = array[left]
        array[left] = pivot

        self.quickSortHelper(array, s, left - 1)

        self.quickSortHelper(array, left + 1, e)




        