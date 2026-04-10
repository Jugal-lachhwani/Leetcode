class Solution:
    def findOrder(self, V: int, pre: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        for i in pre:
            adj[i[0]].append(i[1])
        indegree = [0 for i in range(V)]
        topo = []
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            topo.append(cur)
            for j in adj[cur]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
                    
        return topo[::-1] if len(topo) == V else []