class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0
        for i in range(len(arr)):
            curSum += arr[i]
            if arr[i] > curSum:
                curSum = arr[i]
            maxSum = max(curSum, maxSum)

        return maxSum