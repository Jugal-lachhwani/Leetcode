class Solution:
    def minimumEffortPath(self,grid: List[List[int]]) -> int:
        q = deque()
        di = [0,0,1,-1]
        dj = [1,-1,0,0]
        n = len(grid)
        m = len(grid[0])
        min_effort = float("inf")
        self.vis = [[float('inf') for i in range(m)] for j in range(n)]
        min_effort = float('-inf')
        self.vis[0][0] = 0
        q.append((0,0,0))
        
        while q:
            i,j,effort = q.popleft()
              
            for o in range(len(di)):
                a,b = i+di[o], j+dj[o]

                if a >= 0 and b >= 0 and a < len(grid) and b < len(grid[0]): 
                    if  max(abs(grid[a][b] - grid[i][j]), effort) < self.vis[a][b]:
                        self.vis[a][b] = max(abs(grid[a][b] - grid[i][j]), effort)
                        q.append((a,b,max(abs(grid[a][b] - grid[i][j]), effort)))
                     
        return self.vis[n-1][m-1]