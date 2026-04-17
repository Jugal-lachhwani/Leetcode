class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)
        for i in range(len(queries)):
            target = queries[i]

            if nums[target] not in d or len(d[nums[target]]) == 1:
                ans[i] = -1
                continue
            arr = d[nums[target]]
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    break
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            left = arr[mid - 1] if mid > 0 else arr[-1]
            right = arr[mid + 1] if mid < len(arr) - 1 else arr[0]

            def dist(a, b):
                return min(abs(a - b), n - abs(a - b))


            ans[i] = min(dist(target, left), dist(target, right))
        return ans