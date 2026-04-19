class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        next_dp = [[0 for i in range(m)] for j in range(m)]
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    next_dp[j1][j2] = grid[n-1][j1]
                else:
                    next_dp[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        print(next_dp)

        for i in range(n-2,-1,-1):
            cur_dp = [[0 for i in range(m)] for j in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    if j1 == j2:
                        cur_sum = grid[i][j1]
                    else:
                        cur_sum = grid[i][j1] + grid[i][j2]
                    max_sum = float('-inf')
                    for ind1 in (1,0,-1):
                        for ind2 in (1,0,-1):
                            newj1,newj2 = j1 + ind1, j2 + ind2
                            if 0 <= newj1 < m and 0 <= newj2 < m:
                                max_sum = max(max_sum,next_dp[newj1][newj2]+ cur_sum)
                            
                    cur_dp[j1][j2] = max_sum
                
            next_dp = cur_dp
        
        return next_dp[0][m-1]