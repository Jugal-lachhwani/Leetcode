class Solution:
    def getSneakyNumbers(self, n: List[int]) -> List[int]:
        c = 0
        l = set()
        r = []
        for i in n:
            if len(r) > 2:
                return
            if i in l:
                r.append(i)
            l.add(i)
        return r