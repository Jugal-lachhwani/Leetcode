class Solution:
    def majorityElement(self, a: List[int]) -> int:
        a.sort()
        return a[len(a)//2]