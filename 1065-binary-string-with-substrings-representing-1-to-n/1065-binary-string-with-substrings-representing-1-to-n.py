class Solution:
    def queryString(self, s: str, n: int) -> bool:
        d = deque()
        d.append('1')
        for i in range(1,n+1):
            d1 = d.popleft()
            if d1 not in s:
                return False
            d.append(d1 + '0')
            d.append(d1 + '1')
        
        return True