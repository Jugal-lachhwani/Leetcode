class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n+1:
            return False
        s = set(nums)
        c = 0
        for i in range(1,n+2):
            if i != n+1 and i not in s:
                return False
            if nums[i-1] == n:
                c+=1
        return c == 2
