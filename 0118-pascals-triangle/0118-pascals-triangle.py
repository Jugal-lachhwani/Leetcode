class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        for i in range(numRows-1):
            l_copy = l[i].copy()
            l_copy.append(0)
            l_copy.insert(0,0)
            l1 = []
            for i in range(len(l_copy)- 1):
                l1.append(l_copy[i] + l_copy[i+1])
            l.append(l1)

        return l
