class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        q = []
        n = len(grid)
        heapq.heappush(q,(grid[0][0],0,0))
        di = [0,1,-1,0]
        dj = [1,0,0,-1]
        vis = [[0 for i in range(n)] for _ in range(n)]
        vis[0][0] = True
        while q:
            t,i,j = heapq.heappop(q)
            if i == n-1 and j == n-1:
                return t
            for idx in range(4):
                new_i,new_j = i+di[idx],j+dj[idx]
                if 0 <= new_i < n and 0 <= new_j < n and vis[new_i][new_j] == False:
                    heapq.heappush(q, (max(grid[new_i][new_j],t),new_i,new_j))
                    vis[new_i][new_j] = True
            
