class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev, x = 0, n
        while x > 0:
            r = x%10
            x = x//10
            rev = 10 * rev + r
        return abs(n-rev)
