class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        
        # there are 4 directions need to think of. 
        # top left 
        
        for i in range(rows): 
            for j in range(cols): 
                if matrix[i][j] != 0: 
                    top  = matrix[i-1][j] if i > 0 else float('inf')
                    left = matrix[i][j-1] if j > 0 else float('inf')
                    matrix[i][j] = min(top, left) + 1 
        
        # bottom right
        for i in range(rows)[::-1]:
            for j in range(cols)[::-1]: 
                if matrix[i][j] != 0:
                    bot   = matrix[i+1][j] if i+1 < rows else float('inf')
                    right = matrix[i][j+1] if j+1 < cols else float('inf')
                    matrix[i][j] = min(matrix[i][j],min(bot, right) + 1)
        
        return matrix 
                        