class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        max_sum = float("-inf")
        
        for i in range(n):
            if i <= 1:
                dp[i] = nums[i]
                max_sum = max(max_sum, dp[i])
                continue
            if i <= 2:
                dp[i] = dp[i-2] + nums[i]
                max_sum = max(max_sum, dp[i])
                continue         
            first =  dp[i-2] + nums[i]
            second = dp[i-3] + nums[i]
            dp[i] = max(first,second)
            max_sum = max(max_sum, dp[i])
        return max_sum