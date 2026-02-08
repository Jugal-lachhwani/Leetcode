class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def nqueens(col,lower_row,lower_diagonal,upper_diagonal,n,res,board):
            if col == n:
                res.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                if lower_row[row] == 0 and lower_diagonal[row + col] == 0 and upper_diagonal[n-1+col-row] == 0:
                    board[row][col] = 'Q'
                    lower_row[row] = lower_diagonal[row + col] = upper_diagonal[n-1+col-row] = 1
                    nqueens(col+1,lower_row,lower_diagonal,upper_diagonal,n,res,board)
                    
                    lower_row[row] = lower_diagonal[row + col] = upper_diagonal[n-1+col-row] = 0
                    board[row][col] = '.'

        res = []
        board = [["." for i in range(n)] for _ in range(n)]
        lower_row = [0 for i in range(n)]
        lower_diagonal = [0 for i in range(n * 2 - 1)]
        upper_diagonal = [0 for i in range(n * 2 - 1)]
        
        nqueens(0,lower_row,lower_diagonal,upper_diagonal,n,res,board)
        
        return res