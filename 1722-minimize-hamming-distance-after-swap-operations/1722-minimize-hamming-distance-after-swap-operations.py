class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        components = []
        n = len(source)
        adj = [[] for _ in range(n)]

        for i,j in allowedSwaps:
            adj[i].append(j)
            adj[j].append(i)

        q = deque()
        vis = [False for i in range(n)]
        count = 0
        for i in range(n): 
            if vis[i] == False:
                s_count = Counter()
                t_count = Counter()
                q.append(i)
                vis[i] = True
                while q:
                    cur = q.popleft()
                    s_count[source[cur]] += 1
                    t_count[target[cur]] += 1
                    for j in adj[cur]:
                        if not vis[j]:
                            q.append(j)
                            vis[j] = True
                            
                for val in s_count:
                    if val in t_count:
                        count += max(0, s_count[val] - t_count[val])
                    else:
                        count += s_count[val]
            
        return count
            
            


