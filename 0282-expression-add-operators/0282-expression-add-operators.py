class Solution:
    def addOperators(self, nums: str, target: int):
        res = []
        n = len(nums)

        def dfs(ind, expr, value, last):
            if ind == n:
                if value == target:
                    res.append(expr)
                return

            for i in range(ind, n):
                # prevent leading zero numbers
                if i != ind and nums[ind] == '0':
                    break

                num_str = nums[ind:i+1]
                num = int(num_str)

                if ind == 0:
                    dfs(i + 1, num_str, num, num)
                else:
                    # +
                    dfs(i + 1,
                        expr + "+" + num_str,
                        value + num,
                        num)

                    # -
                    dfs(i + 1,
                        expr + "-" + num_str,
                        value - num,
                        -num)

                    # *
                    dfs(i + 1,
                        expr + "*" + num_str,
                        value - last + last * num,
                        last * num)

        dfs(0, "", 0, 0)
        return res
