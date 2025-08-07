class Solution:
    def maxProfit(self, a: List[int]) -> int:
        p = 0
        for i in range(1,len(a)):
            if(a[i] > a[i-1]):
                p += a[i] - a[i-1]
        return p