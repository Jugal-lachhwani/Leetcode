class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for i in str(num):
                ans.append(int(i))
        return ans
            