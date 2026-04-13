class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        abs_val = float("inf")
        for i in range(len(nums)):
            if nums[i] == target and abs(i - start) < abs_val:
                abs_val = abs(i - start)
        return abs_val