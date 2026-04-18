class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        prev = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[i] = 1
                    continue

                num1 = 0
                if i-1 >= 0:
                    num1 = prev[j] 
                num2 = 0
                if j-1 >= 0:
                    num2 = temp[j-1]
                temp[j] = num1 + num2
            prev = temp
        return prev[-1]