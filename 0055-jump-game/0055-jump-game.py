class Solution:
    def canJump(self, a: List[int]) -> bool:
        i = 0
        j = a[0]
        while i < len(a) and j >= 0:
            if i == len(a)-1:
                return True
            elif a[i] > j:
                j = a[i]
            elif j == 0:
                return False
            i +=1
            j -= 1
        return True
