class DS:
    def __init__(self,V):
        self.parent = [i for i in range(V+1)]
        self.size = [1 for i in range(V+1)]

    def getParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.getParent(self.parent[u])
        return self.parent[u]
            
    def UnionBySize(self, u, v):
        pu = self.getParent(u)
        pv = self.getParent(v)
        
        if pu == pv:
            return
        
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
    
    def getSize(self, u):
        return self.size[self.getParent(u)]

class Solution:
    def isValid(self, i, j, n):
        # Return false if pixel is invalid
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= n:
            return False
        # Return true if pixel is valid
        return True

    def addInitialIslands(self, grid, ds, n):
        delRow = [1, 0]
        delCol = [0, 1]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                
                for i in range(2):
                    adjr = delRow[i] + row
                    adjc = delCol[i] + col
                
                    if self.isValid(adjr,adjc, n) and grid[adjr][adjc] == 1:
                        nodeNo = row * n + col
                        adjNodeNo = adjr * n + adjc
                        ds.UnionBySize(nodeNo, adjNodeNo)
                    
    def largestIsland(self, grid):
        n = len(grid)
        delRow = [-1,0,1, 0]
        delCol = [0,-1,0, 1]
        ds = DS(n*n)
        
        self.addInitialIslands(grid, ds, n)
        ans = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                components = set()
                for i in range(4):
                    adjr = delRow[i] + row
                    adjc = delCol[i] + col
                
                    if self.isValid(adjr,adjc, n) and grid[adjr][adjc] == 1:
                        adjNodeNo = adjr * n + adjc
                        components.add(ds.getParent(adjNodeNo))
                        
                sizeTotal = 0
                    
                for i in components:
                    sizeTotal += ds.size[i]
                    
                ans = max(ans, sizeTotal + 1)
                    
        for cellNo in range(n * n):
            if ds.parent[cellNo] == cellNo:
                ans = max(ans, ds.getSize(cellNo))
        
        # Return the answer
        return ans
        