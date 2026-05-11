class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        # max_num = float('-inf')
        dp = [[-1] * 2 for i in range(n+1)]
        # if arr[0] < 0:
        #     dp[0][1] = 1
        #     dp[0][0] = arr[0]
        #     first_neg = True     
        # elif arr[0] > 0:
        #     dp[0][1] = arr[0]
        #     dp[0][0] = arr[0]
        #     first_neg = False
        # else:
        #     dp[0][1] = 1
        #     dp[0][0] = 1
        #     first_neg = False
        dp[0][0] = 1
        dp[0][1] = 1
        max_num = float('-inf')
        first_neg = False  
        for i in range(1,n+1):
            if arr[i-1] == 0:
                dp[i][0] = 1
                dp[i][0] = 1
                max_num = max(0,max_num)
                first_neg = False
            elif arr[i-1] < 0 and first_neg == False:
                dp[i][0] = dp[i-1][0] * arr[i-1]
                dp[i][1] = 1
                max_num = max(dp[i][0], max_num)
                first_neg = True
            else:
                dp[i][0] = dp[i-1][0] * arr[i-1]
                dp[i][1] = dp[i-1][1] * arr[i-1]
                max_num = max(dp[i][0],dp[i][1],max_num,arr[i-1])
            print(max_num)
        return max_num