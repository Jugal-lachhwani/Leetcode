class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 3D DP table
        n = len(grid)
        m = len(grid[0])
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        
        # Base case: last row
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1][j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        # Fill DP table bottom-up
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    maxi = -10**9
                    curr = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            newJ1, newJ2 = j1 + dj1, j2 + dj2
                            if 0 <= newJ1 < m and 0 <= newJ2 < m:
                                maxi = max(maxi, curr + dp[i+1][newJ1][newJ2])
                            else:
                                maxi = max(maxi, -10**9)
                    dp[i][j1][j2] = maxi
        return dp[0][0][m-1]    