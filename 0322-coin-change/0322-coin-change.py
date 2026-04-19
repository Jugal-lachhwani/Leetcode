class Solution:
    def coinChange(self, coins: List[int], k: int) -> int:
        dp = [float("inf") for i in range(k+1)]
        dp[0] = 0
        n = len(coins)
        for amount in range(k+1):
            if amount % coins[0] == 0:
                dp[amount] = amount / coins[0]
        for i in range(n):
            cur = [float("inf") for i in range(k+1)]
            cur[0] = 0
            for amount in range(k+1):
                not_take = dp[amount]
                take = float('inf')
                if coins[i] <= amount:
                    take = 1 + cur[amount - coins[i]]
                cur[amount] = min(not_take, take)
            dp = cur
        return int(dp[-1]) if dp[-1] != float('inf') else -1 