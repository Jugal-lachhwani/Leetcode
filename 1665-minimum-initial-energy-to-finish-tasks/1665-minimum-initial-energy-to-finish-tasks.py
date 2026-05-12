class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: -(x[1] - x[0]))
        min_amt = 0
        re_amt = 0
        for task in tasks:
            actual,minimum = task
            # min_amt += max(0,(minimum - re_amt))
            if re_amt > minimum:
                re_amt = re_amt - actual
            else:
                min_amt += (minimum - re_amt)
                re_amt = minimum-actual
        return min_amt

