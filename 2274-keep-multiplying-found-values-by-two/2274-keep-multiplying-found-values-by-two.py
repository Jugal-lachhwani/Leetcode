class Solution:
    def findFinalValue(self, nums: List[int], orignal: int) -> int:
        s = set(nums)
        while orignal in s:
            orignal *= 2 
        return orignal