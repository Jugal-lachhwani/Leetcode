class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        val = 0
        p = 0
        s = 0
        for i in nums:
            val += (p*i)
            s += i
            p+=1
        p = len(nums) - 1
        max_val = val

        for i in range(p):
            # print(val,s,nums[i],p,(nums[i] * p))
            val = val - s + nums[i] + (nums[i] * p)
            max_val = max(max_val,val)
            
        
        return max_val


