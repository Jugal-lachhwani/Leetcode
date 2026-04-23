class Solution:
    def isAllStars(self, S1, i):
        for j in range(1, i + 1):
            if S1[j - 1] != '*':
                return False
        return True
    def isMatch(self, S2, S1):
        n = len(S1)
        m = len(S2)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = False
        for i in range(1, n + 1):
            if self.isAllStars(S1, i):
                for j in range(m + 1):
                    dp[i][j] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1] or S1[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif S1[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        return dp[n][m]
