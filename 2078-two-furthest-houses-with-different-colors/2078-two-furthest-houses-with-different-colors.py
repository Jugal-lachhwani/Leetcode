class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        j = n - 1
        max_left = float("-inf")
        while i <= j:
            if colors[i] != colors[j]:
                max_left = (j-i)
                break
            j -= 1
        i = 0
        j = n - 1
        max_right = float("-inf")
        while i <= j:
            if colors[i] != colors[j]:
                max_right = (j-i)
                break
            i += 1
        
        return max(max_left,max_right)
        