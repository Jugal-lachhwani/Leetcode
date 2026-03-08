class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        left = 0
        right = 0
        max_count = float('-inf')
        while right >= left and right < len(fruits):
            if fruits[right] not in d:
                if len(d) >= 2:
                    if d[fruits[left]] > 1:
                        d[fruits[left]] -= 1
                    else:
                        del d[fruits[left]]
                    
                    left += 1
                
                else:
                    d[fruits[right]] = 1
                    right += 1
            else:
                d[fruits[right]] += 1
                right += 1
            
            # print(d)
                
            max_count = max(max_count,right - left)
            
            # print(max_count)
        
        return max_count   