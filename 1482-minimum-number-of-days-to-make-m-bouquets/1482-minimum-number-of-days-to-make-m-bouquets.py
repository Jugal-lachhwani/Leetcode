class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        def flowerbed(arr,mid,k,m):
            k_c = 0
            for i in arr:
                if i - mid <= 0:
                    k_c += 1
                    if k == k_c:
                        k_c = 0
                        m-=1
                else:
                    k_c = 0
            return m <= 0
        if k * m > len(arr):
            return -1
        l = 0
        r = max(arr)
        min_num = max(arr)
        while l <= r:
            mid = (l+r) // 2
            b = flowerbed(arr,mid,k,m)
            if b == True:
                min_num = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_num