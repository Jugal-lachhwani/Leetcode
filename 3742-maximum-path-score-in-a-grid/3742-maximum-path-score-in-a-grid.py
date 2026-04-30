class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])

        INF = float("-inf")
        dp = [[[INF] * (k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):

                    if i+1 < m:
                        new_val = grid[i+1][j]
                        cost = 0 if new_val == 0 else 1
                        if cost + c <= k:
                            dp[i+1][j][cost+c] = max(dp[i+1][j][cost+c], dp[i][j][c] + new_val)

                    if j+1 < n:
                        new_val = grid[i][j+1]
                        cost = 0 if new_val == 0 else 1
                        if cost + c <= k:
                            dp[i][j+1][cost+c] = max(dp[i][j+1][cost+c], dp[i][j][c] + new_val)
        
        ans = max(dp[m-1][n-1]) 

        return ans if ans != INF else -1
                        

                
