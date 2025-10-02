class Solution:
    def maxBottlesDrunk(self, n: int, x: int) -> int:
        ans = n
        while n >= x:
            n -= x - 1
            x += 1
            ans += 1
        return ans