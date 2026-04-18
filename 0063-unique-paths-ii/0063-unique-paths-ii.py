class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1:
            return 0
        grid[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    continue
                num1 = 0
                if i-1 >= 0:
                    num1 = grid[i-1][j]
                num2 = 0
                if j-1 >= 0:
                    num2 = grid[i][j-1]
                grid[i][j] = num1 + num2
        return grid[n-1][m-1]