class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            r = 0
            # d = 10
            cur = []
            while num > 0:
                r = num % 10
                num = num // 10
                # d = d * 10
                cur.append(r)
            ans.extend(cur[::-1])
        return ans
            