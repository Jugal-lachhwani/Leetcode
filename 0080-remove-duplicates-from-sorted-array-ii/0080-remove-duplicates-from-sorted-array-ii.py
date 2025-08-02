class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        if len(a) < 3:
            return len(a)
        i = 2
        while i < len(a):
            if a[i] == a[i-1] == a[i-2]:
                a.remove(a[i])
            else:
                i+=1
        return len(a)