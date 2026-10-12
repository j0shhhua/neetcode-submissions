class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        if n == 0 or n == 1:
            return count + 1
            
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
                
        
        
        