class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_increasing(arr):
            curr = arr[0]
            for i in range(1,len(arr)):
                if arr[i] <= curr:
                    return False
                curr = arr[i]
            return True
        
        size = 2*k

        for i in range(len(nums)-size+1):
            j = i+k
            if is_increasing(nums[i:j]) and is_increasing(nums[j:j+k]):
                return True
        return False