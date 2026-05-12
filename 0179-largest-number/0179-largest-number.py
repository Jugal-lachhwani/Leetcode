class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=list(map(str,nums)) 
        n=len(nums)
        for i in range(n): 
            for j in range(i+1,n): 
                if nums[j]+nums[i]>nums[i]+nums[j]: 
                    nums[i],nums[j]=nums[j],nums[i] 
        ans="".join(nums) 
        return '0' if ans[0]=="0" else ans 