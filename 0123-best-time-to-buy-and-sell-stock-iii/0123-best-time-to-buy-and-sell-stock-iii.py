class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahead = [[0] * 3 for _ in range(2)]
        cur = [[0] * 3 for _ in range(2)]
        n = len(prices)
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 0:
                        cur[buy][cap] = max(ahead[0][cap],
                                            -prices[ind] + ahead[1][cap])
                    else:
                        cur[buy][cap] = max(ahead[1][cap],
                                            prices[ind] + ahead[0][cap - 1])
            ahead = [row[:] for row in cur]

        return ahead[0][2]      