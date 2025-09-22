class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        m = 0
        s = 0
        # print(list(d.values()))

        for i in list(d.values()):
            if i > m : 
                m = i
                s = i
            elif i == m:
                s += i

        return s