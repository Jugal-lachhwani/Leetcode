class Solution(object):
    def search(self, nums, target):
        min_val = min(nums)
        s = nums.index(min_val)
        r = len(nums) - 1
        l = 0
        while l <= r:
            print('how')
            mid = (l + r) // 2
            m = nums[(mid + s)%len(nums)]
            print(m)
            if m == target:
                return (mid + s)%len(nums)
            elif m > target:
                r = mid-1
            else:
                l = mid+1
        return -1