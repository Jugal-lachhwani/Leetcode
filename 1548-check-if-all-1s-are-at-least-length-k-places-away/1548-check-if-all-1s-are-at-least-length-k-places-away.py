class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        idx = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if idx != None:
                    if i - idx <= k:
                        return False
                idx = i
        return True
