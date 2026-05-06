class Solution:
    def countSquares(self, dp: List[List[int]]) -> int:
        # dp = matrix.copy()
        n = len(dp)
        m = len(dp[0])
        sum = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0:
                    continue
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                # print(dp[i][j])
                sum += dp[i][j]
        # print(dp)
        return sum