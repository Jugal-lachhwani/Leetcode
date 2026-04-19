class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        i,j = n-1,m-1
        max_dist = 0
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                max_dist = max(max_dist,j-i)
                i -= 1
            else:
                j-=1
                if i > j:
                    i = j
        return max_dist
                
