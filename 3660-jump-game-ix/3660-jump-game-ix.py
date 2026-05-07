class Solution:
    def maxValue(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_arr = [0] * n
        max_num = float("-inf")
        min_arr = [0] * n
        min_num = float("inf")
        # min_idx = -1
        for i in range(n):
            max_num = max(max_num,arr[i])
            max_arr[i] = max_num
        for i in range(n-1,-1,-1):
            min_arr[i] = min(arr[i],min_num)
            min_num = min_arr[i]
        # print(max_arr,min_arr)

        ans = [0] * n

        ans[-1] = max_arr[-1]

        for i in range(n-2,-1,-1):
            if max_arr[i] > min_arr[i+1]:
                ans[i] = ans[i+1]
            else:
                ans[i] = max_arr[i]

        return ans
