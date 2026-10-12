class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        q = []
        checker = {"}":"{", "]":"[", ")":"("}

        for i in s:
            if i in checker:
                if q and q[-1] == checker[i]:
                    q.pop()
                else:
                    return False
            else:
                q.append(i)

        return True if not q else False 

        


        
        