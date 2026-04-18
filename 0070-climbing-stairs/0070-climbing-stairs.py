class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 and n == 1:
            return 1
        
        prev1 = 1
        prev2 = 1
        i = 1
        ans = 1
        while i < n:
            ans = prev1 + prev2
            i += 1
            prev2 = prev1
            prev1 = ans
    
        return ans
