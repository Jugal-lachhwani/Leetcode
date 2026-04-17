class Solution:
    def __init__(self):
        self.timer = 1
    def dfs(self, adj, i,parent, vis, tin, low, bridges):
        vis[i] = 1
        tin[i] = low[i] = self.timer
        self.timer += 1
        for j in adj[i]:
            if j == parent:
                continue
            if vis[j] == 0:
                self.dfs(adj, j,i, vis, tin, low, bridges)
                low[i] = min(low[i], low[j])
                if low[j] > tin[i]:
                    bridges.append((i,j))
            else:
                low[i] = min(low[i], low[j])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for i in range(n)]
        for i,j in connections:
            adj[i].append(j)
            adj[j].append(i)
        vis = [0] * n
        tin = [0] * n
        low = [0] * n
        bridges = []
        self.dfs(adj, 0,0, vis, tin, low, bridges)
        return bridges