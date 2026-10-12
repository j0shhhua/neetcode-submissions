class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ""
        for i in s:
            if i.isalnum():
                test+=i.lower()
        return True if test == test[::-1] else False