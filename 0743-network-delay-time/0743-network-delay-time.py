class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        for i,j,w in times:
            adj[i].append((j,w))
        q = []
        vis = [float('inf') for i in range(n)]   
        vis[k-1] = 0
        heapq.heappush(q, (0,k))
        
        while q:
            price,i = heapq.heappop(q)
            for node,cur_price in adj[i]:
                if price + cur_price < vis[node-1]:
                    vis[node-1] = price + cur_price
                    q.append((vis[node-1], node))
        
        time = float('-inf')
        for i in vis:
            time = max(time, i)
        
               
        return time if time != float('inf') else -1