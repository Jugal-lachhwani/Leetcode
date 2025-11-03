class Solution:
    def minCost(self, c: str, t: List[int]) -> int:
        r = 0
        i = 0
        while i < len(c):
            b = c[i]
            j = i+1
            m = t[i]
            con = 0
            while j < len(c) and c[j] == c[i]:
                con += 1
                if con < 2:
                    ma = max(t[j],m)
                    m = min(t[j],m)
                else:
                    m = min(t[j],ma)
                    ma = max(t[j],ma)
                r+=m
                j+=1
            i = j
        return r