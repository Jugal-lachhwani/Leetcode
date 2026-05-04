class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n//2):
            matrix[i],matrix[n-i-1] = matrix[n-i-1], matrix[i]
        # print(matrix)
        for ind in range(n):
            # print(ind)
            i = ind+1
            while i < n:
                # print(i,ind)
                matrix[ind][i],matrix[i][ind] = matrix[i][ind],matrix[ind][i]
                i+=1
        
        
