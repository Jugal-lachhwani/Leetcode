class Solution:
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
    
        def calculate_k(arr,num):
            sum = 0
            for i in arr:
                sum+= math.ceil(i/num)
            return sum  

        l = 1
        r = max(arr)
        k = max(arr)
        
        while l <= r:
            mid = (l+r) // 2
            h_curr = calculate_k(arr,mid)
            if h_curr <= h:
                r = mid - 1
                k = min(k,mid)
            else:
                l = mid + 1
        return k