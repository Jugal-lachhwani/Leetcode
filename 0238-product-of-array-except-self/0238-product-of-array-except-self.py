class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        m = 1
        count0 = 0
        for i in range(len(a)):
            if a[i] != 0:
                m *= a[i]
            else:
                count0+=1
        if count0 == 0:
            for i in range(len(a)):
                a[i] = int(m/a[i])
        elif count0 == 1:
            for i in range(len(a)):
                if a[i] == 0:
                    a[i] = m
                else:
                    a[i] = 0
        elif count0 > 1:
            for i in range(len(a)):
                a[i] = 0
        return a