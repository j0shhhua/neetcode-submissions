class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        actual = sorted(list(s))
        ctrl = sorted(list(t))

        if actual == ctrl:
            return True
        else:
            return False