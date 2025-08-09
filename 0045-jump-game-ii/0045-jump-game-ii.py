class Solution:
    def jump(self, a: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(a) - 1): 
            farthest = max(farthest, i + a[i]) 
            if i == current_end: 
                jumps += 1
                current_end = farthest  #
            
            if current_end >= len(a) - 1:
                break
        
        return jumps
