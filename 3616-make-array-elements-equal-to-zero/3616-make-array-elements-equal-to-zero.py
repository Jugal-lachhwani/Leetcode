class Solution:
    def countValidSelections(self, l: List[int]) -> int:
        n = len(l)
        count = 0
        for i in range(len(l)):
            if l[i] == 0:
                if abs(sum(l[:i]) - sum(l[i:n])) < 1:
                    count += 2 
                elif abs(sum(l[:i]) - sum(l[i:n])) < 2:
                    count += 1
        return count