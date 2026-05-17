class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis = [0] * n
        q = deque()
        q.append(start)
        vis[start] = 1
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            if (cur + arr[cur]) < n and vis[cur + arr[cur]] == 0:
                q.append((cur + arr[cur]))
                vis[cur + arr[cur]] = 1
            if (cur - arr[cur]) >= 0 and vis[cur - arr[cur]] == 0:
                q.append((cur - arr[cur]))
                vis[cur - arr[cur]] = 1
        return False
