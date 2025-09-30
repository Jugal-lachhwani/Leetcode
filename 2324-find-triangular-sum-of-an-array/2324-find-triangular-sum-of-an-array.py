class Solution:
    def triangularSum(self, l: List[int]) -> int:
        l1 = []
        while len(l) > 1:
            l1 = []
            for i in range(1,len(l)):
                num = (l[i] + l[i-1]) % 10
                l1.append(num)
            l = l1
        return l[0]