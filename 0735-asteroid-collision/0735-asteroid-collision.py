class Solution:
    def asteroidCollision(self, l: List[int]) -> List[int]:
        s = deque()
        for i in l:
            if i > 0:
                s.append(i)
            else:       
                while s:
                    if s[-1] < 0:
                        s.append(i)
                        break
                    if abs(i) == s[-1]:
                        s.pop()
                        break
                    if s[-1] > abs(i):
                        break
                    if s[-1] < abs(i):
                        s.pop()
                else:
                    s.append(i)
        return list(s)