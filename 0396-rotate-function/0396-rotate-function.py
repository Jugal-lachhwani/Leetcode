class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        val = 0
        for i,v in enumerate(nums):
            val += (i*v)
        s = sum(nums)
        max_val = val
        n = len(nums)
        for i in range(n-1):
            val = val - s + (nums[i] * n)
            max_val = max(max_val,val)
            
        
        return max_val


