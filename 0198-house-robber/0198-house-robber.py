class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        max_sum = float("-inf")
        prev1, prev2, prev3 = 0,0,0
        for i in range(n):
            if i <= 1:
                curr = nums[i]
                max_sum = max(max_sum, curr)
                prev3 = prev2
                prev2 = prev1
                prev1 = curr
                continue
            if i <= 2:
                curr = prev2 + nums[i]
                prev3 = prev2
                prev2 = prev1
                prev1 = curr
                max_sum = max(max_sum, curr)
                continue         
            first =  prev2 + nums[i]
            second = prev3 + nums[i]
            curr = max(first,second)
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
            max_sum = max(max_sum, curr)
        return max_sum