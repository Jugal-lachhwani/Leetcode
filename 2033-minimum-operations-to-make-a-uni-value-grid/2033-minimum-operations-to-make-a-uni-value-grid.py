class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        l = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l.append(grid[i][j])
        l.sort()
        length = len(l)
        closest_num = l[length // 2]
        operation = 0
        for i in range(len(l)):
            if abs(l[i] - closest_num) % x != 0:
                return -1
            else:
                operation += abs(l[i] - closest_num) // x
        
        return int(operation)