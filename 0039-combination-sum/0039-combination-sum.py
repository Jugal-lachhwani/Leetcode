class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(i, target, curr):
            if i == len(candidates):
                if target == 0:
                    res.append(curr[:])
                return

            if candidates[i] <= target:
                curr.append(candidates[i])
                backtrack(i, target - candidates[i], curr)
                curr.pop()

            backtrack(i + 1, target, curr)

        backtrack(0, target, [])
        return res